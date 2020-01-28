import boto3
import base64
import json

def lambda_handler(event, context):
    output = [] # Initialize output list
    for record in event['records']:
        # Coded in base64, Retrieve data
        tweet = base64.b64decode(record['data']).decode('utf-8').strip()
        text = json.loads(tweet)["text"] # Get text
        time = json.loads(tweet)["created_at"] # Get time of tweet
        username = json.loads(tweet)["user"]["screenname"] # Get username for author of tweet
        print(username)

        # Using AWS Comprehend, classify message as postive or negative
        comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
        sentiment_all = comprehend.detect_sentiment(Text=text, LanguageCode='en')
        sentiment = sentiment_all['Sentiment']
        print(sentiment)

        # Retrieve positive, negative scores. Subtract to find total score
        positive = sentiment_all['SentimentScore']['Positive']
        negative = sentiment_all['SentimentScore']['Negative']
        score = positive - negative
        print(score)
        
        data_record = {
            'text': text,
            'sentiment': sentiment,
            'score': score,
            'time': time,
            'username': username
        }
        print(data_record)
        
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(json.dumps(data_record).encode('utf-8')).decode('utf-8')
        }
        print(output_record)
        output.append(output_record)

    print(output)
    return {'records': output}