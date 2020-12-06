from nltk.sentiment.vader import SentimentIntensityAnalyzer

def add_sentiment_columns(df, text_col):
    sentiment = SentimentIntensityAnalyzer()
    df['sentiment'] = df[text_col].map(sentiment.polarity_scores)
    df['neg_sent'] = df['sentiment'].map(lambda x: x['neg'])
    df['neu_sent'] = df['sentiment'].map(lambda x: x['neu'])
    df['pos_sent'] = df['sentiment'].map(lambda x: x['pos'])
    df['compound_sent'] = df['sentiment'].map(lambda x: x['compound'])
    df.drop(columns='sentiment', inplace=True)