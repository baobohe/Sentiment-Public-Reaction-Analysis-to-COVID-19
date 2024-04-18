# -*- coding: utf-8 -*-
import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import collections  
import itertools
from gensim import corpora, models
import pprint
from gensim.models import LdaModel
import warnings
warnings.filterwarnings("ignore")


data  = pd.read_csv('Wuhan variant data.csv') #读取的数据
text = data['content'].astype(str) #要分析的文本列
num_topics=5  #主题数
save_name = 'Wuhan' #保存名称前缀
#================预处理============
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords as nltk_stopwords
from emoji import UNICODE_EMOJI, demojize, emojize

replacement_patterns = [
(r'won\'t', 'will not'),
(r'can\'t', 'cannot'),
(r'i\'m', 'i am'),
(r'ain\'t', 'is not'),
(r'(\w+)\'ll', '\g<1> will'),
(r'(\w+)n\'t', '\g<1> not'),
(r'(\w+)\'ve', '\g<1> have'),
(r'(\w+)\'s', '\g<1> is'),
(r'(\w+)\'re', '\g<1> are'),
(r'(\w+)\'d', '\g<1> would')
]
class RegexpReplacer(object):
    def __init__(self, patterns=replacement_patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in
        patterns]
    def replace(self, text):
        s = text
        for (pattern, repl) in self.patterns:
            (s, count) = re.subn(pattern, repl, s)
        return s
replace = RegexpReplacer()
#删除网址
def _remove_url(line):
    line = re.sub("http[s]?:\S+|ftp:\S+|www.\S+",' ', line)
    return line
#删除表情符
def remove_emoji(line):
    line_emoji = [x for x in UNICODE_EMOJI["en"] if x in line]
    for x in line_emoji:
        line = line.replace(x, " ")
    return line
#删除@
def _remove_word1(line):
    line = re.sub(r'(@)(.*?)(\w+)','', line)
    return line
#删除#
def _remove_word2(line):
    line = re.sub(r'(#)(.*?)(\w+)','', line)
    return line
#只保留英文字符，数字，和这些符号
def remove_punctuation(line):
    line = re.sub("[^ ^a-z^A-Z^0-9^_-]",' ', line)
    return line
#替换词汇
def replace_word(x):
    if x in replace_dict.keys():
        return replace_dict[x]
    else:
        return x
#预处理
def deal_line(line):
    line = _remove_url(line)
    line = remove_emoji(line)
    line = _remove_word1(line)
    line = _remove_word2(line)
    line = line.lower() #全部转为小写
    line = replace.replace(line)
    line = remove_punctuation(line)
    #分词
    line = word_tokenize(line)
    #词形还原（归并）
    wnl = WordNetLemmatizer()
    line = [wnl.lemmatize(ws) for ws in line]
    line = [replace_word(w) for w in line]
    #去除停用词
    line = [w for w in line if not w in stopwords and len(w) > 1]
    return line


#替换词典
replace_dict = dict(pd.read_excel('同义词替换.xls')[['old','new']].values)
#停用词典
mystopwords = [line.rstrip().lower() for line in open('mystopwords.txt', encoding='utf-8')]
stopwords = nltk_stopwords.words('english')+mystopwords+[''+' ']

#==开始预处理===
#进行预处理
text_cut = text.map(lambda x:deal_line(x))
#删除预处理后空白的
text_cut = text_cut.loc[text_cut.map(lambda x:len(x)>3)]
text = text.loc[text_cut.index]
data = data.loc[text_cut.index]
text.index = range(text.shape[0])
text_cut.index = range(text_cut.shape[0])
data.index = range(data.shape[0])
#保存预处理结果
pd.DataFrame({'text':text,'text_cut':text_cut.map(lambda x:' '.join(x))}).to_excel(save_name+'分词结果.xlsx')

#==词频统计
all_words = list(itertools.chain(*text_cut)) #全部的单词
word_counts = collections.Counter(all_words)  #做词频统计
word_counts_top = word_counts.most_common()# 获取前N最高频的词####-------------重要的
pd.DataFrame(word_counts_top,columns=['word','count']).to_excel(save_name+'词频统计结果.xlsx',index=0) #保存词频统计结果

#=================lda=========
#==向量化处理===
dictionary = corpora.Dictionary(text_cut) #字典词频统计
dictionary.filter_extremes(no_below=data.shape[0]/500,no_above=0.5)#删除出现小于30的词,删除出现比率大于50%的词
corpus = [dictionary.doc2bow(words) for words in text_cut] #词频向量化
print(len(dictionary))

lda =  LdaModel(
                corpus=corpus,
                id2word=dictionary,
                alpha='auto',
                eta='auto',
                iterations=300,
                num_topics=num_topics,
                random_state =1
                )

#展示主题
pprint.pprint(lda.show_topics(num_topics=num_topics,num_words=15))

#===保存主题-词分布
topic = []
for i in range(num_topics):
    topic.append(np.array(lda.show_topic(i,topn=100))[:,0])
    topic.append(np.array(lda.show_topic(i,topn=100))[:,1])
topic = pd.DataFrame(topic).T
topic.columns = list(itertools.chain(*[['topic{}_word'.format(i),'topic{}_distribution'.format(i)] for i in range(num_topics)]))
topic.to_excel(save_name+'LDA主题-词分布.xlsx')


#===保存文档-主题分布
data_lda = lda.get_document_topics(corpus,minimum_probability=0)
data_lda = pd.DataFrame([dict(data_lda[i]) for i in range(data.shape[0])])
data_lda.columns=['topic{}'.format(i) for i in range(num_topics)]
for i in range(num_topics):
    data['topic{}'.format(i)] = data_lda['topic{}'.format(i)].values
data['max_topic'] = np.argmax(data[['topic{}'.format(i) for i in range(num_topics)]].values,axis=1)
data.to_excel(save_name+'数据+lda结果.xlsx',index=0)









