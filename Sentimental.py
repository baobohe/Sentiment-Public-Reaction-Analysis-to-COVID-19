from textblob import TextBlob
import pandas as pd


# Perform sentimental analysis toward Wuhan variant tweets
Wuhan = pd.read_csv('Wuhan variant data.csv')
all_content = ''
for i in range(len(Wuhan['content'])):
    all_content = all_content + str(Wuhan['content'][i])
WuhanLDA = pd.read_csv('WuhanLDA主题-词分布.csv')
all_keywords1 = ''
for i in range(len(WuhanLDA['topic0_word'])):
    all_keywords1 = all_keywords1 + str(WuhanLDA['topic0_word'][i] + ',')
all_keywords2 = ''
for i in range(len(WuhanLDA['topic1_word'])):
    all_keywords2 = all_keywords2 + str(WuhanLDA['topic1_word'][i] + ',')
all_keywords3 = ''
for i in range(len(WuhanLDA['topic2_word'])):
    all_keywords3 = all_keywords3 + str(WuhanLDA['topic2_word'][i] + ',')
all_keywords4 = ''
for i in range(len(WuhanLDA['topic1_word'])):
    all_keywords4 = all_keywords4 + str(WuhanLDA['topic3_word'][i] + ',')
all_keywords5 = ''
for i in range(len(WuhanLDA['topic1_word'])):
    all_keywords5 = all_keywords5 + str(WuhanLDA['topic4_word'][i] + ',')

all_keyword = all_keywords1 + all_keywords2 + all_keywords3 + all_keywords4 + all_keywords5
text = all_content + all_keyword
# print(text)
blob1 = TextBlob(all_content)
blob2 = TextBlob(all_keyword)
sentiment_content = blob1.sentiment.polarity
sentiment_keyword = blob2.sentiment.polarity
# Calculate the final score based on 70% of content score and 30% of keyword score.
Omicron_score = (sentiment_content * 0.7 + sentiment_keyword * 0.3) * 1000






# Perform sentimental analysis toward Alpha variant tweets
Alpha = pd.read_csv('Alpha variant data.csv')
all_content = ''
for i in range(len(Alpha['content'])):
    all_content = all_content + str(Alpha['content'][i])
AlphaLDA = pd.read_csv('AlphaLDA主题-词分布.csv')
all_keywords1 = ''
for i in range(len(AlphaLDA['topic0_word'])):
    all_keywords1 = all_keywords1 + str(AlphaLDA['topic0_word'][i] + ',')
all_keywords2 = ''
for i in range(len(AlphaLDA['topic1_word'])):
    all_keywords2 = all_keywords2 + str(AlphaLDA['topic1_word'][i] + ',')
all_keywords3 = ''
for i in range(len(AlphaLDA['topic2_word'])):
    all_keywords3 = all_keywords3 + str(AlphaLDA['topic2_word'][i] + ',')
all_keywords4 = ''
for i in range(len(AlphaLDA['topic1_word'])):
    all_keywords4 = all_keywords4 + str(AlphaLDA['topic3_word'][i] + ',')
all_keywords5 = ''
for i in range(len(AlphaLDA['topic1_word'])):
    all_keywords5 = all_keywords5 + str(AlphaLDA['topic4_word'][i] + ',')

all_keyword = all_keywords1 + all_keywords2 + all_keywords3 + all_keywords4 + all_keywords5
text = all_content + all_keyword
# print(text)
blob1 = TextBlob(all_content)
blob2 = TextBlob(all_keyword)
sentiment_content = blob1.sentiment.polarity
sentiment_keyword = blob2.sentiment.polarity
# Calculate the final score based on 70% of content score and 30% of keyword score.
Alpha_score = (sentiment_content * 0.7 + sentiment_keyword * 0.3) * 1000






# Perform sentimental analysis toward Delta variant tweets
Delta = pd.read_csv('Delta variant data.csv')
all_content = ''
for i in range(len(Delta['content'])):
    all_content = all_content + str(Delta['content'][i])
DeltaLDA = pd.read_csv('DeltaLDA主题-词分布.csv')
all_keywords1 = ''
for i in range(len(DeltaLDA['topic0_word'])):
    all_keywords1 = all_keywords1 + str(DeltaLDA['topic0_word'][i] + ',')
all_keywords2 = ''
for i in range(len(DeltaLDA['topic1_word'])):
    all_keywords2 = all_keywords2 + str(DeltaLDA['topic1_word'][i] + ',')
all_keywords3 = ''
for i in range(len(DeltaLDA['topic2_word'])):
    all_keywords3 = all_keywords3 + str(DeltaLDA['topic2_word'][i] + ',')
all_keywords4 = ''
for i in range(len(DeltaLDA['topic1_word'])):
    all_keywords4 = all_keywords4 + str(DeltaLDA['topic3_word'][i] + ',')
all_keywords5 = ''
for i in range(len(DeltaLDA['topic1_word'])):
    all_keywords5 = all_keywords5 + str(DeltaLDA['topic4_word'][i] + ',')

all_keyword = all_keywords1 + all_keywords2 + all_keywords3 + all_keywords4 + all_keywords5
text = all_content + all_keyword
# print(text)
blob1 = TextBlob(all_content)
blob2 = TextBlob(all_keyword)
sentiment_content = blob1.sentiment.polarity
sentiment_keyword = blob2.sentiment.polarity
# Calculate the final score based on 70% of content score and 30% of keyword score.
Delta_score = (sentiment_content * 0.7 + sentiment_keyword * 0.3) * 1000






# Perform sentimental analysis toward Omicron variant tweets
Omicron = pd.read_csv('Omicron variant data.csv')
all_content = ''
for i in range(len(Omicron['content'])):
    all_content = all_content + str(Omicron['content'][i])
OmicronLDA = pd.read_csv('OmicronLDA主题-词分布.csv')
all_keywords1 = ''
for i in range(len(OmicronLDA['topic0_word'])):
    all_keywords1 = all_keywords1 + str(OmicronLDA['topic0_word'][i] + ',')
all_keywords2 = ''
for i in range(len(OmicronLDA['topic1_word'])):
    all_keywords2 = all_keywords2 + str(OmicronLDA['topic1_word'][i] + ',')
all_keywords3 = ''
for i in range(len(OmicronLDA['topic2_word'])):
    all_keywords3 = all_keywords3 + str(OmicronLDA['topic2_word'][i] + ',')
all_keywords4 = ''
for i in range(len(OmicronLDA['topic1_word'])):
    all_keywords4 = all_keywords4 + str(OmicronLDA['topic3_word'][i] + ',')
all_keywords5 = ''
for i in range(len(OmicronLDA['topic1_word'])):
    all_keywords5 = all_keywords5 + str(OmicronLDA['topic4_word'][i] + ',')

all_keyword = all_keywords1 + all_keywords2 + all_keywords3 + all_keywords4 + all_keywords5
text = all_content + all_keyword
# print(text)
blob1 = TextBlob(all_content)
blob2 = TextBlob(all_keyword)
sentiment_content = blob1.sentiment.polarity
sentiment_keyword = blob2.sentiment.polarity
# Calculate the final score based on 70% of content score and 30% of keyword score.
Wuhan_score = (sentiment_content * 0.7 + sentiment_keyword * 0.3) * 1000





# Print final statement.
print('COVID-19 Wuhan strain receives a sentimental score of', round(Wuhan_score, 2), 'out of 100.')
print('COVID-19 Alpha strain receives a sentimental score of', round(Alpha_score, 2), 'out of 100.')
print('COVID-19 Delta strain receives a sentimental score of', round(Delta_score, 2), 'out of 100.')
print('COVID-19 Omicron strain receives a sentimental score of', round(Omicron_score, 2), 'out of 100.')


import numpy as np
# Summarizing details of share, like, and retweet for Wuhan strain
share_column_Wuhan = pd.DataFrame(Wuhan, columns = ['share'])
share_column_Wuhan['share'] = share_column_Wuhan['share'].replace(np.nan, 0)
# print(sum(share_column_Wuhan['share'])) 5408

retweet_column_Wuhan = pd.DataFrame(Wuhan, columns = ['retweet'])
retweet_column_Wuhan['retweet'] = retweet_column_Wuhan['retweet'].replace(np.nan, 0)
# print(sum(retweet_column_Wuhan['retweet'])) 68149

like_column_Wuhan = pd.DataFrame(Wuhan, columns = ['like'])
like_column_Wuhan['like'] = like_column_Wuhan['like'].replace(np.nan, 0)
# print(sum(like_column_Wuhan['like'])) 310343

# Summarizing details of share, like, and retweet for Alpha strain
share_column_Alpha = pd.DataFrame(Alpha, columns = ['share'])
share_column_Alpha['share'] = share_column_Alpha['share'].replace(np.nan, 0)
# print(sum(share_column_Alpha['share'])) 58663

retweet_column_Alpha = pd.DataFrame(Alpha, columns = ['retweet'])
retweet_column_Alpha['retweet'] = retweet_column_Alpha['retweet'].replace(np.nan, 0)
# print(sum(retweet_column_Alpha['retweet'])) 89211

like_column_Alpha = pd.DataFrame(Alpha, columns = ['like'])
like_column_Alpha['like'] = like_column_Alpha['like'].replace(np.nan, 0)
# print(sum((like_column_Alpha['like']))) 454536


# Summarizing details of share, like, and retweet for Delta strain
share_column_Delta = pd.DataFrame(Delta, columns = ['share'])
share_column_Delta['share'] = share_column_Delta['share'].replace(np.nan, 0)
# print(sum(share_column_Delta['share'])) 35776

retweet_column_Delta = pd.DataFrame(Delta, columns = ['retweet'])
retweet_column_Delta['retweet'] = retweet_column_Delta['retweet'].replace(np.nan, 0)
# print(sum(retweet_column_Delta['retweet'])) 139206

like_column_Delta = pd.DataFrame(Delta, columns = ['like'])
like_column_Delta['like'] = like_column_Delta['like'].replace(np.nan, 0)
# print(sum((like_column_Delta['like']))) 611139



# Summarizing details of share, like, and retweet for Omicron strain
share_column_Omicron = pd.DataFrame(Omicron, columns = ['share'])
share_column_Omicron['share'] = share_column_Omicron['share'].replace(np.nan, 0)
# print(sum(share_column_Omicron['share'])) 21283

retweet_column_Omicron = pd.DataFrame(Omicron, columns = ['retweet'])
retweet_column_Omicron['retweet'] = retweet_column_Omicron['retweet'].replace(np.nan, 0)
# print(sum(retweet_column_Omicron['retweet'])) 50572

like_column_Omicron = pd.DataFrame(Delta, columns = ['like'])
like_column_Omicron['like'] = like_column_Omicron['like'].replace(np.nan, 0)
# print(sum((like_column_Omicron['like']))) 611139



# Now refine the score with the formula: original_score + sum_share / 100000 + sum_retweet / 100000 + sum_like / 100000
score_with_srl_Wuhan = Wuhan_score + sum(share_column_Wuhan['share']) / 100000 \
                                   + sum(retweet_column_Wuhan['retweet']) / 100000 \
                                   + sum(like_column_Wuhan['like']) / 100000
print('Refined score of Wuhan is', round(score_with_srl_Wuhan,2), 'out of 100.')


score_with_srl_Alpha = Alpha_score + sum(share_column_Alpha['share']) / 100000 \
                                   + sum(retweet_column_Alpha['retweet']) / 100000 \
                                   + sum(like_column_Alpha['like']) / 100000
print('Refined score of Alpha is', round(score_with_srl_Alpha,2), 'out of 100.')


score_with_srl_Delta = Delta_score + sum(share_column_Delta['share']) / 100000 \
                                   + sum(retweet_column_Delta['retweet']) / 100000 \
                                   + sum(like_column_Delta['like']) / 100000
print('Refined score of Delta is', round(score_with_srl_Delta,2), 'out of 100.')



score_with_srl_Omicron = Omicron_score + sum(share_column_Omicron['share']) / 100000 \
                                   + sum(retweet_column_Omicron['retweet']) / 100000 \
                                   + sum(like_column_Omicron['like']) / 100000
print('Refined score of Omicron is', round(score_with_srl_Omicron,2), 'out of 100.')
