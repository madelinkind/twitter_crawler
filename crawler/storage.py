import os
import sys
import abc
from tweepy.models import Status as TweepyStatus
import json

# Django specific settings
sys.path.append('./orm')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# import and setup django
import django
django.setup()

# Import your models for use in your script
from db.models import Tweet, TwitterUser


class IStorage(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def save_tweet(self, tweet: object) -> bool:
        pass


class DBStorage(IStorage):
    def __init__(self, *args, **kwargs):
        super(DBStorage, self).__init__(*args, **kwargs)

    def save_tweet(self, tweet: TweepyStatus) -> bool:
        # get all tweets metadata from specific user
        t = Tweet()
        t.tweet_lang = tweet.lang
        t.is_retweet = tweet.retweeted
        t.tweet_text = tweet.text
        t.tweet_date = tweet.created_at
        t.retweet_count = tweet.retweet_count
        t.tweet_id = tweet.id

        t.tweet_info = tweet._json
        
        if hasattr(tweet, 'retweeted_status'):
            t.is_retweet = True
        else:
            t.is_retweet = False
        try:
            user = TwitterUser.objects.get(screen_name=tweet.user.screen_name)
            t.twitter_user = user
        except TwitterUser.DoesNotExist as ex:
            print(ex.message)
            return False

        t.save()
        return True
