from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
from pymongo import MongoClient
import json
import time

## to obtain this infomation, you must create a twitter account and a twitter application at dev.twitter.com
ckey = '<insert key here>'
csecret = '<insert secret here>'
atoken =  '<insert token here>'
asecret = '<insert token secret here>'


#Listener Class Override
class listener(StreamListener):
    def on_data(self,data):
        try:
            client = MongoClient('localhost', 27017) # these are just mongodb defaults
            db = client['mexico'] # database name; will be created if it does not exist 
            collection = db['twitter'] # collection name (a collection is the no-sql analogue of a table basically; will be created if it does not exit
            tweet = json.loads(data)
            if (tweet['geo'] != None) and (tweet['place']['country_code'] == 'MX'): # ensure the document has geography and get only those in Mexico; there is quite a bit of overlap with the USA
                collection.insert(tweet)
                print 'Record inserted'
            else:
                print 'Not in Mexico'
            return True
        except BaseException, e:
            print 'failed ondata,', str(e)
            pass
    def on_error(self, status):
        print statuses

auth = OAuthHandler(ckey,  csecret)
auth.set_access_token(atoken,  asecret)

def start_stream():
    while True: # include while statement here so that the stream automatically restarts on error
        try:
            twitterStream = Stream(auth, listener())
            twitterStream.filter(locations=[-120.92,13.23,-85.40,33.83]) # scrape by location (Mexico)
        except:
            continue

start_stream()
