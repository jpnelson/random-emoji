import tweepy, random, threading

from emoji import get_emoji_list
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

def get_random_emoji():
    emoji_list = get_emoji_list()
    emoji = random.choice(emoji_list)
    emoji_unicode_escaped = "\\U%08x" % emoji
    return emoji_unicode_escaped.decode('unicode-escape')

def make_tweet():
    tweet = get_random_emoji() + get_random_emoji()
    if (random.random() <= 0.1):
        tweet += get_random_emoji()

    return tweet

#enter the corresponding information from your Twitter application:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def tweet():
    api.update_status(make_tweet())


tweet()
set_interval(tweet, 60 * 60 * 3)
