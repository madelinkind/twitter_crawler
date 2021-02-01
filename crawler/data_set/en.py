# Import your models for use in your script
from db.models import Tweet, TwitterUser
import demo 

list_users = demo.users_list

# Lists of Data(X) and Class(y) in (en)
X = []
y = []
for user in list_users:
    user_name = TwitterUser.objects.get(screen_name=user)
    for tweet in Tweet.objects.filter(twitter_user=user_name.id).all():
        if not tweet.is_retweet and tweet.tweet_lang == 'en':
            X.append(tweet.tweet_text)
            y.append(tweet.twitter_user)