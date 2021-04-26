import sys
import datetime

try:
    from django.db import models
except Exception:
    print("Exception: Django Not Found, please install it with \"pip install django\".")
    sys.exit()

# Create your models here.

class TwitterUser(models.Model):
    screen_name = models.CharField(max_length=15)
    type_user = models.CharField(max_length=20, null=True)
    # twitter_user_id = models.CharField(max_length=20, null=True)
    # user_info = models.JSONField()
    # followers_count = models.IntegerField(null=True)

    class Meta:
        db_table = "twitter_users"

class Tweet(models.Model):
    twitter_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet_text = models.CharField(max_length=280)
    tweet_date = models.DateTimeField()
    tweet_lang = models.CharField(max_length=3, null=True)
    tweet_id = models.CharField(db_index=True, max_length=20, null=True)
    tweet_info = models.JSONField()
    is_retweet = models.BooleanField(default=True)
    retweet_count = models.IntegerField(null=True)

    class Meta:
        db_table = "tweets"
