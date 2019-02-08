import tweepy
from config import *
from os.path import join as pjoin
import pandas as pd
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
df = pd.DataFrame(columns=['created_at', 'key', 'text'])
count = 0
for tweet in tweepy.Cursor(api.search,
                           q="jenasena",
                           rpp=100,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
    #print(tweet.created_at, tweet.text)
    q = 'jenasena'
    df = df.append({'created_at': tweet.created_at, 'key': q,
                    'text': tweet.text}, ignore_index=True)

df.to_csv(pjoin('data', 'test_' + str(100) + q + '.csv'))
print('-Done-')
