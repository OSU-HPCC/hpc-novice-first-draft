from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import csv
import datetime

## to obtain this infomation, you must create a twitter account and a twitter application at dev.twitter.com
ckey = '<insert key here>'
csecret = '<insert secret here>'
atoken =  '<insert token here>'
asecret = '<insert token secret here>'

class listener(StreamListener):
    
    def on_data(self, data):
        print 'running' # print some info to ensure the user that the script is running
        with open('/home/user/data/twitter-scrape-' + datetime.datetime.now().strftime("%y%m%d") + '.json', 'a') as f: # save the data with the date (this is useful when scraping over many days)
            writer = csv.writer(f)
            writer.writerow([str(data)])
        return True
        
    def on_error(self,  status):
        print status
        print datetime.datetime.now()
        
        
auth = OAuthHandler(ckey,  csecret)
auth.set_access_token(atoken,  asecret)
twitterStream = Stream(auth,  listener())
twitterStream.filter(track=["car"]) # scrape by a term
# twitterStream.filter(locations=[-103.38,33.41,-94.05,37.24]) # scrape by location (Oklahoma)
#twitterStream.filter(locations=[-125.00,24.00,-65.00,49.00]) # scrape by location (USA)
