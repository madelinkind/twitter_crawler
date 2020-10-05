import logging
from typing import Tuple, Dict
from datetime import datetime, date, time, timedelta
from collections import Counter

from tweepy import OAuthHandler, API, Cursor

import os
import sys

# Django specific settings
sys.path.append('./orm')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# import and setup django
import django
django.setup()

# Import your models for use in your script
from db.models import Tweet



class TwitterEngine(object):
    """
        Tutorials:
        . https://blog.f-secure.com/how-to-get-tweets-from-a-twitter-account-using-python-and-tweepy/

        Twitter User object reference: 
        . https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/user-object

        Populate users from friends:
        . https://stackoverflow.com/questions/8058858/how-to-get-all-users-in-a-list-twitter-api

        Query API:
        . https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/
    """

    def __init__(self, *args, **kwargs):
        # init parent class
        super(TwitterEngine, self).__init__()

        # get Twitter API keys from named parameters
        access_token = kwargs['access_token']
        access_token_secret = kwargs['access_token_secret']
        consumer_key = kwargs['consumer_key']
        consumer_key_secret = kwargs['consumer_key_secret']
        usernames = kwargs['usernames']

        # users list must be valid
        if not usernames or not isinstance(usernames, list):
            raise ValueError('Users list must be provided') 

        # set instance variables
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.consumer_key = consumer_key
        self.consumer_key_secret = consumer_key_secret
        self.usernames = usernames
        self.TwitterApi = None

        # initialize api to communicate with Twitter
        self.__init_twitter_api()

    # NOTE: constructor "overload" example
    # @classmethod
    # def from_json(cls, book_as_json: str) -> TwitterEngine:
    #     return TwitterEngine()

    def __init_twitter_api(self) -> None:
        auth = OAuthHandler(self.consumer_key, self.consumer_key_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.TwitterApi = API(auth)

    # ------------------------

    def download_tweets(self) -> None:
        for username in self.usernames:
            # download tweets of a specific user 
            user_tweets_info = self.get_user_tweets(username)

            # TODO: Store this information (wether FileSystemStorage or DBStorage, use interface)

    def get_user_tweets(self, username: str) -> Tuple[bool, Dict[str, object]]:
        # check username
        if not username:
            logging.warning(f"Invalid username: ${username}!")
            return False, {}

        print(f"Downloading tweets for username: '${username}'")

        # get user tweets
        user_id = self.get_user_id_from_username(username)
        all_hashtags = []
        all_mentions = []
        user_tweets = []
        tweet_count = 0
        # end_date = datetime.utcnow() - timedelta(days=30)
        
        # get all tweets metadata from specific user
        for tweet_info in Cursor(self.TwitterApi.user_timeline, id=user_id).items():
            t = Tweet()
            t.tweet_text = tweet_info.text
            t.tweet_date = tweet_info.created_at
            t.tweet_id = 10 # tweet_info.id
            t.tweet_info = '[]'
            t.twitter_users_id = 2
            t.save()

            continue

            tweet_count += 1
            user_tweets.append(tweet_info)

            # if tweet metadata doesn't have entities, continue
            if not hasattr(tweet_info, "entities"):
                continue

            entities = tweet_info.entities

            # get current tweet hashtags
            tweet_hashtags = self.get_tweet_hashtags(entities)
            all_hashtags += tweet_hashtags

            # get current tweet mentions
            tweet_mentions = self.get_tweet_mentions(entities)
            all_mentions += tweet_mentions

            # # restricting to accounts created after specific date (i.e., in the last month)
            # if status.created_at < end_date:
            #     break

        # get 10 most common mentions in tweet
        common_mentions = [(item, count) for item, count in Counter(all_mentions).most_common(10)]

        # get 10 most used hastags
        common_hashtags = [(item, count) for item, count in Counter(all_hashtags).most_common(10)]

        user_tweets_info = {
            'tweets_count': tweet_count,
            'tweets': user_tweets,

            'common_mentions': common_mentions,
            'all_mentions': all_mentions,

            'common_hashtags': common_hashtags,
            'all_hashtags': all_hashtags,
        }

        return True, user_tweets_info

    def get_user_id_from_username(self, username: str) -> str:
        # https://stackoverflow.com/questions/29223454/user-id-to-username-tweepy
        # https://www.geeksforgeeks.org/python-api-get_user-in-tweepy/

        # user = self.TwitterApi.get_user(screen_name=username)
        # return user.id
        return username

    def get_tweet_hashtags(self, tweet_entities) -> list:
        if "hashtags" not in tweet_entities:
            return []

        hashtags = []
        for ent in tweet_entities["hashtags"]:
            # entity must be valid and 'text' provided
            if ent is None or "text" not in ent:
                continue

            hashtag = ent["text"]
            if hashtag:
                hashtags.append(hashtag)

        return hashtags
    
    def get_tweet_mentions(self, tweet_entities) -> list:
        if "user_mentions" not in tweet_entities:
            return []

        mentions = []
        for ent in tweet_entities["user_mentions"]:
            if ent is None or "screen_name" not in ent:
                continue

            name = ent["screen_name"]
            if name:
                mentions.append(name)

        return mentions
