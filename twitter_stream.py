import settings #local file
import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import json #data
import time #sleep
import re #regex

## setup twitter-api access
# goto https://apps.twitter.com/ to generate the keys
auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_key_secret)
auth.set_access_token(settings.access_token, settings.access_token_secret)
api = tweepy.API(auth)

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        tweetData = json.loads(data.strip())
        print tweetData


    def on_error(self, status):
        #error number 503, servers down
        print "error ", status

    # def handle_tweetData(self, tweetData):
    #     tweet = tweetData.get("text")
    #     username = tweetData.get("user").get("screen_name")
    #     followers = tweetData.get("user").get("followers_count")
    #     retweet_test = tweet[0] + tweet[1]
    #
    #     if (followers > 500 and retweet_test.lower() != 'rt'):
    #         print ("@" + username + ": has " + str(followers) + " followers, tweets: " + tweet + "").encode('utf8')



if __name__ == '__main__':
    #This handles Twitter authentification and the connection to Twitter Streaming API
    l = StdOutListener()

    stream = Stream(auth, l)
    stream.filter(track=['rocket league', 'rocketleague', '#rocketleague'])

    # stream.filter(track=['chance to #win', 'chance to win', 'follow to #win', 'follow to win',
    #                         'retweet to #win', 'retweet to win', 'rt to #win', 'rt to win',
    #                         'follow to enter', 'retweet to #enter', 'retweet to enter', 'rt to #enter',
    #                         'rt to enter', '#winitwednesday', '#winwednesday', '#winningwednesday'])
