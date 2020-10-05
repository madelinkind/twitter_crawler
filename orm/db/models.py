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
    twitter_user_id = models.IntegerField(null=True)
    user_info = models.JSONField()

    class Meta:
        db_table = "twitter_users"

class Tweet(models.Model):
    twitter_users = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet_text = models.CharField(max_length=280)
    tweet_date = models.DateTimeField()
    tweet_id = models.IntegerField()
    tweet_info = models.JSONField()

    class Meta:
        db_table = "tweets"
