import os
import sys

from crawler.io import load_users_list_from_file
import crawler.config as conf
from crawler.engine import TwitterEngine
from crawler.storage import DBStorage
# from datetime import datetime, date, time, timedelta

# ----------------------------------------------------------

# Django specific settings
sys.path.append('./orm')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# import and setup django
import django
django.setup()

# Import your models for use in your script
from db.models import Tweet, TwitterUser

# ----------------------------------------------------------

# # load users list

users_map = map(lambda item: item['screen_name'], TwitterUser.objects.order_by('id').values('screen_name'))
users_list = list(users_map)

dbs = DBStorage()
te = TwitterEngine(
    access_token = conf.ACCESS_TOKEN,
    access_token_secret = conf.ACCESS_TOKEN_SECRET,
    consumer_key = conf.CONSUMER_KEY,
    consumer_key_secret = conf.CONSUMER_KEY_SECRET,
    usernames = users_list,

    storage = dbs
)

te.download_tweets()