#!/usr/bin/env python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
import sys
sys.path.append(".")
import config
from helpers import build_tweet_url

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

def search_tweets(query: str):
    #-----------------------------------------------------------------------
    # perform a basic search 
    # Twitter API docs:
    # https://dev.twitter.com/rest/reference/get/search/tweets
    #-----------------------------------------------------------------------
    results = twitter.search.tweets(q = f'"{query}"')

    #-----------------------------------------------------------------------
    # How long did this query take?
    #-----------------------------------------------------------------------
    print("Search complete (%.3f seconds)" % (results["search_metadata"]["completed_in"]))

    # search results with expected fields
    cleaned_results = []

    #-----------------------------------------------------------------------
    # loop through each of the tweets in the search statuses, and print their details
    #-----------------------------------------------------------------------
    for result in results["statuses"]:
        
        id, text, created_at, user, retweet_count, favorite_count = result["id"], result["text"], result["created_at"], result['user']["screen_name"], result["retweet_count"], result["favorite_count"]

        # build tweet url 
        tweet_url = build_tweet_url(id)

        tweet = { 
            "id": id, 
            "text": text, 
            "created_at": created_at, 
            "user": user,
            "retweet_count": retweet_count,
            "favorite_count": favorite_count,
            "tweet_url": tweet_url
        }

        cleaned_results.append(tweet)

    return cleaned_results