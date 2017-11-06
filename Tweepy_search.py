#!/usr/bin/env python3.6
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey='V7NMDq4w2jqY3XfuhVMQIus6U'
csecret='Fh91YD6XAui8Cv37bwDVJa1IwdFUAtavIUpzLHHLiz7OE1SY84'
atoken='886811149156491265-MiLUyDvaI2tdsRjhk0s1X8bVTnChTSQ'
asecret='KfuBI33I2pPxez2llydllT8qSZJPLBHbW485hNAYz3VOg'

class listener(StreamListener):
   
     def on_data(self, data):
        print(data)
        return True
     def on_error(self, status):
         print(status)

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

twitterStream = Stream(auth,listener())
twitterStream.filter(track=['Iphone X'])

def to_df():
	

