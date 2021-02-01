import logging
from typing import Tuple, Dict
from datetime import datetime, date, time, timedelta
from collections import Counter
import time
from tweepy import OAuthHandler, API, Cursor

# from db.models import Tweet, TwitterUser

import os
import sys

# Django specific settings
sys.path.append('./orm')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# import and setup django
import django
django.setup()

# Import your models for use in your script
from db.models import Tweet, TwitterUser

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

        storage = kwargs['storage']

        # users list must be valid
        if not usernames or not isinstance(usernames, list):
            raise ValueError('Users list must be provided') 

        # set instance variables
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.consumer_key = consumer_key
        self.consumer_key_secret = consumer_key_secret
        self.usernames = usernames
        self.storage = storage
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
    #
    def user_saved_tweets_count(self, username):
        tweets_count = Tweet.objects.filter(twitter_user=username.id).count()
        return tweets_count
    #
    def current_tweet_db_is_older(self, tweet_date_db_recent, tweet_date_api_recent):
        if tweet_date_db_recent >= tweet_date_api_recent:
            return True
        return False

    def get_user_tweets(self, username: str) -> bool:

        # maximum allowed amount of tweets to download the API
        TIMELINE_MAX = 3200
        success = False
        # check username
        if not username:
            logging.warning(f"Invalid username: {username}!")
            return False
        
        print(f"Downloading tweets for username: '{username}'")

        time.sleep(5)

        user_name = TwitterUser.objects.get(screen_name=username)
        tweet_date_db_recent = None
        #
        if Tweet.objects.filter(twitter_user=user_name.id).order_by('-tweet_date').exists():
            tweet_date_db_recent = Tweet.objects.filter(twitter_user=user_name.id).order_by('-tweet_date')[0].tweet_date
            
        user_timeline = Cursor(self.TwitterApi.user_timeline, id=username).items()
        for tweet_info in user_timeline:
            tweet_date_api_recent = tweet_info.created_at
            # 
            if tweet_date_db_recent is not None and self.user_saved_tweets_count(user_name) > TIMELINE_MAX and self.current_tweet_db_is_older(tweet_date_db_recent, tweet_date_api_recent):
                    break
            
            # tween already saved
            if Tweet.objects.filter(tweet_id=tweet_info.id).exists():
                continue

            # need to add tweet to db
            print(f"{datetime.now()}: Saving tweet with id={tweet_info.id}")
            success = self.storage.save_tweet(tweet_info)

            if not success:
                print("The tweet already exists in data base")

            continue

        return True
