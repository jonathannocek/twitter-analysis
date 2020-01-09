import tweepy

# Import file containing private keys to access Twitter API
import credentials

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_status(self, status):
        print(status.text)
    
    def on_error(self, status_code):
         if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

MyStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener)

myStream.filter(track=['python'])