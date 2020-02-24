import TwitterSearch
import credentials
import geopy
import time
import os
import json

def search(query):
    try:
        tso = TwitterSearch.TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords(query) # let's define all words we would like to have a look for
        tso.set_language('en') # we want to see English tweets only
        tso.set_include_entities(False) # and don't give us all those entity information
        
        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch.TwitterSearch(
            consumer_key = credentials.consumer_key,
            consumer_secret = credentials.consumer_secret,
            access_token = credentials.access_token,
            access_token_secret = credentials.access_token_secret
        )

        # Initialize output
        output = [] 

        # this is where the fun actually starts :)
        for tweet in ts.search_tweets_iterable(tso):
            text = tweet['text']
            username = tweet["user"]["screen_name"]
            # Format datetime so Kibana reads it
            created_at = tweet["created_at"] 
            datetime = time.strftime('%Y-%m-%dT%H:%M:%S', time.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y'))

            data = {
            'text': text,
            'datetime': datetime,
            'username': username
            }
            
            output.append(data)

        with open('data.json', 'w') as f:
            json.dump(output, f)



    except TwitterSearch.TwitterSearchException as e: 
        print(e)

if __name__ == '__main__':
    query = ['Elon Musk','-filter:retweets', '-filter:replies']
    search(query)