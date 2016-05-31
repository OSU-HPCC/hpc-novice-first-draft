# -*- coding: utf-8 -*-
"""Created on Thu Oct  8 18:03:52 2015

@author: matt

Purpose: Parses geolocated point tweets from a raw .csv file"""
#See https://dev.twitter.com/overview/api/users for information about fields and their meanings

import sys
import csv
import time
from itertools import izip

start_time = time.time()

def parse_tweets(raw_tweet_file, parsed_tweet_file):

    # Create new .csv with headers
    with open(parsed_tweet_file, 'w+') as f2:
        fieldnames = ['tweet_time','twitter_id','tweet_text','twitter_client','os_type','coordinates','lat','lon',
                                    'city_state','country','place_type','full_place_name','country_code','language',
                                    'timestamp','user_id','screen_name','followers_count','friends_count','listed_count',
                                    'favorites_count','profile_creation_date','utc_offset','time_zone']
        writer = csv.DictWriter(f2,fieldnames=fieldnames)
        writer.writeheader()
        
    counter = 0
    
    with open(raw_tweet_file, 'rb') as f1: # Open the raw/cleaned tweet file
        reader = csv.reader(f1) # Create a reader so that the raw data can be read
        for row in reader: # For every row
            counter = counter + 1 # For displaying row number
            if '"geo":{"type":"Point",' in str(row): # If geoloaction type is a point (we only want points)
                try:
                    tweet_time = row[0].split('{"created_at":"')[1].split('","id":')[0]; # Tweet time
                except:
                    tweet_time = 'NA'
                    
                try:
                    twitter_id = row[0].split('","id":')[1].split(',"id_str":"')[0];  # Twitter ID or tweet ID?       
                except:
                    twitter_id = 'NA'
                    
                try: 
	            tweet_text = row[0].split('"text":"')[1].split('","source":"')[0]; # The text of the tweet, content
                    if ';' in str(tweet_text):
			tweet_text = tweet_text.translate(None, ';')
		except:
                    tweet_text = 'NA'
                    
                try:
                    os_type = row[0].split('\u003eTwitter for ')[1].split('\\u003c\\/a\\u003e')[0]
               	    twitter_client = 'Twitter' 
		except:
                    source = row[0].split('"source":',1)[1].split('"truncated":')[0]
		    if 'echofon' in str(source):
                        os_type = 'iPhone'
			twitter_client = 'Echofon'
                    elif 'tweetlogix' in str(source):
                        os_type = 'iPhone'
			twitter_client = 'tweetlogix'
                    elif 'tweetmyjobs' in str(source):
                        os_type = 'NA'
			twitter_client = 'tweetmyjobs'
                    elif 'instagram' in str(source):   
			os_type = 'NA'
			twitter_client = 'Instagram'
                    elif 'Twidere for Android' in str(source):
                        os_type = 'Android'
			twitter_client = 'Twidere'
                    elif 'twitter.com' in str(source):
			os_type = 'NA'
			twitter_client = 'twitter.com' 
		    elif 'www.sigalert.com'in str(source):
			os_type = 'NA'
			twitter_client = 'sigalert.com'
	            elif 'Tweetbot for' in str(source):
			os_type = 'iPhone'
			twitter_client = 'Tweetbot' 
		    elif 'foursquare.com' in str(source):
			os_type = 'NA'
			twitter_client = 'Foursquare'
		    elif 'Fenix for Android' in str(source):
			os_type = 'Android'
			twitter_client = 'Fenix'		    
		    elif 'myvinny' in str(source):
			os_type = 'NA'
			twitter_client = 'Vinny'
		    elif 'sandaysoft.com' in str(source):
			os_type = 'NA'
			twitter_client = 'Sandaysoft Cumulus'
		    elif 'dlvr.it' in str(source):
			os_type = 'NA'
			twitter_client = 'dlvr'
		    elif 'dinehere.us' in str(source):
			os_type = 'NA'
			twitter_client = 'dinehere.us'
		    elif 'WxTweeter' in str(source):
			os_type = 'NA'
			twitter_client = 'WxTwitter'
		    elif 'tweetcaster' in str(source):
			os_type = source.split('TweetCaster for' )[1].split('\u003c')[0]
			twitter_client = 'TweetCaster'
		    elif 'untappd' in str(source):
			os_type = 'NA'
			twitter_client = 'Untappd' 
		    else:    
                        os_type = 'NA'
                   	twitter_client = 'NA'
			#twitter_client = 'source' #could split here if we want specific information about tweets we may be missing 
                try:
                    coordinates = row[0].split('"Point","coordinates":[')[1].split(']},"coordinates":{"')[0] # latitude and longitude (to be split next)
                except:
                    coordinates = 'NA'
                    
                try:
                    lat = coordinates.split(',')[0] # latitude
                except:
                    lat = 'NA'
                    
                try:
                    lon = coordinates.split(',')[1] # longitude
                except:
                    lon = 'NA'
                    
                try: 
                    city_state = row[0].split('","full_name":"')[1].split('","country_code":"')[0]
                except:
                    city_state = 'NA'
                    
                try:
                    country = row[0].split('","country":"')[1].split('","bounding_box":')[0]
                except:
                    country = 'NA'
                    
                try:
                    place_type = row[0].split('","place_type":"')[1].split('","name":"')[0] # What follows is for place_type = 'city'
                except:
                    place_type = 'NA'
                    
                try:    
                    full_place_name = row[0].split('","full_name":"')[1].split('","country_code":"')[0] # City, State
                except:
                    full_place_name = 'NA'                    
                    
                try:
                    country_code = row[0].split('","country_code":"')[1].split('","country":')[0] # Country code 
                except:
                    country_code = 'NA'
                    
                try:    
	            language = row[0].split(',"lang":',1)[1][1:6] # User-defined language
	 	    if 'fil' in str(language):
	 		language = 'fil'
	 	    elif 'msa' in str(language):
	 		language = 'msa'
	 	    elif 'zh-tw' in str(language):
	 		language = 'zh-tw'
	 	    elif 'zh-cn' in str(language):
	 		language = 'zh-cn'
	 	    elif 'en-gb' in str(language):
	 		language = 'en-gb'
	 	    else: 
			language = language[0:2]
                except:
                    language = 'NA'
                
                try:                 
                    timestamp = row[0].split('","timestamp_ms":"')[1] # Tweet time; can't split by anything on the right hand side because the tweet ends here

                    timestamp13 = str(timestamp)[0:13] # Take the first 13 characters
                except:
                    timestamp13 = 'NA'
                    
                try:
                    user_id = row[0].split(',"user":{"id":')[1].split(',"id_str":"')[0] 
                except:
                    user_id = 'NA'
                    
                try:    
                    screen_name = row[0].split('","screen_name":"')[1].split('","location":')[0] # screen name
                except:
                    screen_name = 'NA'
                    
                try:
                    followers_count = row[0].split(',"followers_count":')[1].split(',"friends_count":')[0] # Number of followers
                except:
                    followers_count = 'NA'
                    
                try:
                    friends_count = row[0].split(',"friends_count":')[1].split(',"listed_count":')[0] # Number of followees?
                except:
                    friends_count = 'NA'
                    
                try:
                    listed_count = row[0].split(',"listed_count":')[1].split(',"favourites_count":')[0] # No. of public lists the user is a member of 
                except:
                    listed_count = 'NA'
                
                try: 
                    favorites_count = row[0].split(',"favourites_count":')[1].split(',"statuses_count":')[0] # Number of tweets the user has favorited 
                except:
                    favorites_count = 'NA'
                    
                try:
                    profile_creation_date = row[0].split(',"created_at":"')[1].split('","utc_offset":')[0] # Profile creation date
                except:
                    profile_creation_date = 'NA'
                try:
                    utc_offset = row[0].split('","utc_offset":')[1].split(',"time_zone":')[0] # UTC offset
                except:
                    utc_offset = 'NA'
                    
                try:
                    time_zone = row[0].split(',"time_zone":"')[1].split('","geo_enabled":')[0] # User defined time zone
                except:
                    time_zone = 'NA'
                
                with open(parsed_tweet_file, 'a') as f2:
                    writer = csv.writer(f2)
                    writer.writerows(izip([tweet_time],[twitter_id],[tweet_text],[twitter_client],[os_type],[coordinates],[lat],[lon],
                                    [city_state],[country],[place_type],[full_place_name],[country_code],[language],
                                    [timestamp13],[user_id],[screen_name],[followers_count],[friends_count],[listed_count],
                                    [favorites_count],[profile_creation_date],[utc_offset],[time_zone]))

if __name__ == "__main__":
    first_arg = sys.argv[1] # Read first argument from the terminal
    second_arg = sys.argv[2] # Read second argument from the terminal
    parse_tweets(first_arg,second_arg)
