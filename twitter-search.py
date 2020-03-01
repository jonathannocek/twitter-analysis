import TwitterSearch
import credentials
import geopy
import time
import json
import textblob
from textblob.classifiers import NaiveBayesClassifier

def search(query):
    try:
        tso = get_twitter_search_object()
        ts = connect_to_twitter_search()

        # Initialize output
        output = [] 

        # Create Naive Bayes NLP Sentiment model
        training_data = gather_training_data()
        classifier = NaiveBayesClassifier(training_data)

        for tweet in ts.search_tweets_iterable(tso):
            text = tweet['full_text']
            username = tweet["user"]["screen_name"]
            created_at = tweet["created_at"] 
            datetime = time.strftime('%Y-%m-%dT%H:%M:%S', time.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y'))

            blob = textblob.TextBlob(text, classifier=classifier)
            sentiment = blob.classify()

            followers = tweet['user']['followers_count']

            favorites = tweet['favorite_count']
            retweets = tweet['retweet_count']

            data = {
            'text': text,
            'datetime': datetime,
            'username': username,
            'followers': followers,
            'sentiment': sentiment,
            'favorites': favorites,
            'retweets': retweets
            }
            
            output.append(data)

        with open('data.json', 'w') as f:
            json.dump(output, f)

    except TwitterSearch.TwitterSearchException as e: 
        print(e)



def gather_training_data():
    '''
    Trains a natural language processing model using the following data:
    https://pythonprogramming.net/static/downloads/short_reviews/positive.txt
    https://pythonprogramming.net/static/downloads/short_reviews/negative.txt
    '''
    training_data = [] # Initialize list
    with open("train/positive.txt","r") as f:
        for line in f.read().split('\n'):
            classify = (line, 'pos')
            training_data.append(classify)
    with open("train/negative.txt","r") as f:
        for line in f.read().split('\n'):
            classify = (line, 'neg')
            training_data.append(classify)
    return training_data


def get_twitter_search_object():
    '''
    Creates TwitterSearchOrder object from TwitterSearch and returns it
    '''
    tso = TwitterSearch.TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(query) 
    tso.set_language('en') # we want to see English tweets only
    tso.set_include_entities(False) # and don't give us all those entity information
    tso.arguments.update({'tweet_mode':'extended'})
    return(tso)


def connect_to_twitter_search():
    '''
    Connects to Twitter API using private keys
    '''
    ts = TwitterSearch.TwitterSearch(
        consumer_key = credentials.consumer_key,
        consumer_secret = credentials.consumer_secret,
        access_token = credentials.access_token,
        access_token_secret = credentials.access_token_secret
    )
    return(ts)

if __name__ == '__main__':
    # Search for tweet containing 'Elon Musk' w/ no retweets or replies
    query = ['Elon Musk','-filter:retweets', '-filter:replies']
    search(query)