import tweepy, random

from emoji import get_emoji_list
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

def get_random_emoji():
    emoji_list = get_emoji_list()
    emoji = random.choice(emoji_list)
    print emoji
    return unichr(emoji)

def make_tweet():
    tweet = get_random_emoji() + get_random_emoji()
    if (random.random() <= 0.1):
        tweet += get_random_emoji()

    return tweet

#enter the corresponding information from your Twitter application:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


api.update_status(make_tweet())
