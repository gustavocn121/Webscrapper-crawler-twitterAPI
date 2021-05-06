import tweepy
from tweepy_keys import *
import json


def get_mentions_timeline():
    mentions = api.mentions_timeline(wait_on_rate_limit=True)
    return mentions


def get_retweets_of_me():
    rt_me = api.retweets_of_me()
    return rt_me


def twitter_auth():
    auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_KEY_SECRET)
    auth.set_access_token(ACESS_TOKEN, ACESS_TOKEN_SECRET)
    return auth


if __name__ == "__main__":
    api = tweepy.API(twitter_auth(), wait_on_rate_limit=True)
    rt_of_me = get_retweets_of_me()
    for rt in rt_of_me:
        print(rt.text)
