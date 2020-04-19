import tweepy
import boto3
import json

# Import file containing private keys to access Twitter API and AWS
import credentials

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)

api = tweepy.API(auth)

# Authenticate with AWS
client = boto3.client(
    "firehose",
    region_name="us-east-1",
    aws_access_key_id=credentials.aws_access_key_id,
    aws_secret_access_key=credentials.aws_secret_access_key,
)

# Name for AWS Kinesis Firehose stream
streamName = "twitter-stream"

# override tweepy.StreamListener to add logic
class MyStreamListener(tweepy.StreamListener):
    def on_connect(self):
        print("You're connected to the streaming server.")

    def on_data(self, data):
        # Exclude retweets
        if (not json.loads(data)["retweeted"]) and (
            "RT @" not in json.loads(data)["text"]
        ):
            # Filter for tweets that contain 'Trump'
            if "Coronavirus" in json.loads(data)["text"]:
                client.put_record(DeliveryStreamName=streamName, Record={"Data": data})
                print(json.loads(data)["text"])

        return True

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False if on_error disconnects the stream
            return False


if __name__ == "__main__":

    listener = MyStreamListener()
    auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
    auth.set_access_token(credentials.access_token, credentials.access_token_secret)

    # Locations: Longitude and Latitude coordinates for where the tweets will be streamed.
    # First two are southwest corner and the second two are the northeast corner.
    locations = [
        -124.7771694,
        24.520833,
        -66.947028,
        49.384472,  # Contiguous US
        -164.639405,
        58.806859,
        -144.152365,
        71.76871,  # Alaska
        -160.161542,
        18.776344,
        -154.641396,
        22.878623,
    ]  # Hawaii

    stream = tweepy.Stream(auth, listener)
    # Filter by location
    stream.filter(locations=locations)
