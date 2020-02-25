import TwitterSearch
import credentials
import geopy
import time
import json
import textblob

def search(query):
    try:
        tso = TwitterSearch.TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords(query) 
        tso.set_language('en') # we want to see English tweets only
        tso.set_include_entities(False) # and don't give us all those entity information
        
        ts = TwitterSearch.TwitterSearch(
            consumer_key = credentials.consumer_key,
            consumer_secret = credentials.consumer_secret,
            access_token = credentials.access_token,
            access_token_secret = credentials.access_token_secret
        )

        # Initialize output
        output = [] 

        for tweet in ts.search_tweets_iterable(tso):
            text = tweet['text']
            username = tweet["user"]["screen_name"]
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

def train_model():
    '''
    Trains a natural language processing model using the following data:
    https://pythonprogramming.net/static/downloads/short_reviews/positive.txt
    '''
    training_data = [] # Initialize list
    with open("train/positive.txt","r") as f:
        for line in f.read().split('\n'):
            classify = {
                'text': line,
                'label': 'pos'
            }
            training_data.append(classify)
    with open("train/negative.txt","r") as f:
        for line in f.read().split('\n'):
            classify = {
                'text': line,
                'label': 'neg'
            }


if __name__ == '__main__':
    query = ['Elon Musk','-filter:retweets', '-filter:replies']