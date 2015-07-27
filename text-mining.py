#!/usr/bin/python

import sys
import ConfigParser

#import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

class Utils:
    @staticmethod
    def ConfigSectionMap(section):
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1

if __name__ == '__main__':

    try:
        with open('./conf.ini') as f:
            config = ConfigParser.ConfigParser()
            config.read('./conf.ini')    
            u = Utils()
    except:
        raise ValueError("exception: no config.ini file found with appropriate setup - try looking into _config.ini")

    consumer_key = u.ConfigSectionMap('ApiSetup')['api_key']
    consumer_secret = u.ConfigSectionMap('ApiSetup')['api_secret']
    access_token = u.ConfigSectionMap('ApiSetup')['access_token_key']
    access_token_secret = u.ConfigSectionMap('ApiSetup')['access_token_secret']

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    if (len(sys.argv) <= 1):
	print("exception: no argument defined - use 'python text-mining.py arg1...' form")
    else:
#        print(len(sys.argv))
        stream.filter(track=sys.argv[1:])
