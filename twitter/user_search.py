#-----------------------------------------------------------------------
# twitter-user-search
#  - performs a search for users matching a certain query
#-----------------------------------------------------------------------

from flask import jsonify
from twitter import *

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
# import sys
# sys.path.append(".")
import config
from helpers import build_user_url

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

#-----------------------------------------------------------------------
# perform a user search 
# twitter API docs: https://dev.twitter.com/rest/reference/get/users/search
#-----------------------------------------------------------------------
def search_users(query: str):
    results = twitter.users.search(q = f'"{query}"')

    # search results with expected fields
    cleaned_results = []

    #-----------------------------------------------------------------------
    # loop through each of the users, and print their details
    #-----------------------------------------------------------------------
    for user in results:
        # print("@%s (%s): %s" % (user["screen_name"], user["name"], user["location"]))
        # found user brief infos
        id, name, screen_name, created_at, description, location, url, followers_count, friends_count, statuses_count = user["id"], user["name"], user["screen_name"], user["created_at"], user["description"], user["location"], user["url"], user["followers_count"], user["friends_count"], user["statuses_count"]

        # build user url
        user_url = build_user_url(id)

        user = { 
            "id": id, 
            "user_name": name , 
            "screen_name": screen_name,
            "created_at": created_at, 
            "description": description,
            "location": location, 
            "url": url, 
            "followers_count": followers_count, 
            "friends_count": friends_count, 
            "statuses_count": statuses_count,
            "user_url": user_url
        }

        cleaned_results.append(user)

    return cleaned_results
