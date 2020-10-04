from crawler.io import load_users_list_from_file
import crawler.config as conf
from crawler.engine import TwitterEngine

# ----------------------------------------------------------

# success, users_list = load_users_list_from_file(conf.USERS_LIST)
# if not success:
#     print("Failed to load users list")

# print(users_list)

# ----------------------------------------------------------

# load users list
success, users_list = load_users_list_from_file(conf.USERS_LIST)
if not success:
    print("Failed to load users list")

te = TwitterEngine(
    access_token = conf.ACCESS_TOKEN,
    access_token_secret = conf.ACCESS_TOKEN_SECRET,
    consumer_key = conf.CONSUMER_KEY,
    consumer_key_secret = conf.CONSUMER_KEY_SECRET,
    usernames = users_list,
)

te.download_tweets()