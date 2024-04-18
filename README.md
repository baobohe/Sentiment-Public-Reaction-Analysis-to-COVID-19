# Sentiment Public Reaction Analysis to COVID-19 Strains

This project is the culmination of a sentiment analysis conducted on Twitter data, focusing on public reactions to different strains of the COVID-19 virus.

## Overview

This research was conducted as part of an internship at Wuhan University's School of Information Management. By employing a blend of unsupervised and supervised machine learning techniques, we analyzed vast Twitter datasets to glean insights into public sentiment related to the pandemic's evolution.

### Data Preprocessing

- **Extraction, Cleaning, and Tokenization**: We utilized Octoparse and Python's NLTK package to prepare the data.
- **Topic Modeling with LDA**: The Gensim library in Python facilitated the training of an LDA model on the dataset, with a focus on extracting five primary topics.

### Sentiment Analysis

- **Gradient Boosting Machines (GBM)**: We trained a LightGBM model on a dataset of 1.6 million labeled tweets, incorporating the topics to predict sentiment scores.
- **Score Averaging**: Sentiments were averaged across 4,000 data points per variant.

### Key Findings

- The sentiment scores were refined using metrics such as shares, retweets, and likes.
- Scores revealed a trend towards more positive public sentiment as the virus mutated from the Wuhan strain to the Omicron variant.
- Factors such as governmental policies and vaccination drives contributed to the shifting sentiment.

## Repository Structure

```plaintext
.
├── Analysis Scripts/
│   ├── LDA_Topic_Modeling.py
│   ├── Gradient_Boosting_Sentiment_Classification.py
│   └── Data_Cleaning_and_Preprocessing.py
├── Data/
│   ├── Cleaned_Twitter_Dataset.csv
│   ├── LDA_Model_Results.xlsx
│   └── Sentiment_Scores.xlsx
└── Results/
    ├── Detailed_Sentiment_Analysis_Report.pdf
    └── Presentation_Slides.pptx
