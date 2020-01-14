import tweepy
import boto3
import json

# Import file containing private keys to access Twitter API
import credentials

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)

streamName = 'test-stream'

# Authenticate with AWS
client = boto3.client('firehose', region_name='us-east-1',
                          aws_access_key_id=credentials.aws_access_key_id,
                          aws_secret_access_key=credentials.aws_secret_access_key
                          )


api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):

        client.put_record(DeliveryStreamName=streamName,Record={'Data': json.loads(data)["text"]})
        
        print(json.loads(data)["text"])

        return True

    def on_status(self, status):
        print(status.text)
    
    def on_error(self, status_code):
         if status_code == 420:
            #returning False in on_error disconnects the stream
            return False


if __name__ == '__main__':

    listener = MyStreamListener()
    auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
    auth.set_access_token(credentials.access_token, credentials.access_token_secret)
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['donald trump'])