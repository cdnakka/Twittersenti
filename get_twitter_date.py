from config import *
import tweepy
import json
from os.path import join as pjoin
import pandas as pd
data_path = "data"
# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
max_tweets = 5
query = 'jenasena'
searched_tweets = [
    status._json for status in tweepy.Cursor(
        api.search,
        q=query).items(max_tweets)]
json_strings = [json.dumps(json_obj) for json_obj in searched_tweets]

with open(pjoin(data_path,'sample.json'),'w') as f:
    f.write(json_strings[0])

