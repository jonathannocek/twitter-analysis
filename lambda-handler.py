import boto3
import base64
import json
import time

def lambda_handler(event, context):

    output = [] # Initialize output list
    for record in event['records']:
        # Coded in base64, Retrieve data
        tweet = base64.b64decode(record['data']).decode('utf-8').strip()
        text = json.loads(tweet)["text"] 
        username = json.loads(tweet)["user"]["screen_name"]
        
        created_at = json.loads(tweet)["created_at"] 
        date_raw = time.strftime('%Y-%m-%d,%H:%M:%S', time.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y'))
        date_list = [x.strip() for x in date_raw.split(',')]
        date = date_list[0]
        hour = date_list[1]


        # Get city, state
        location_raw = json.loads(tweet)['place']['full_name']
        location = [x.strip() for x in location_raw.split(', ')]
        city = location[0]
        state = location[1]

        # Using AWS Comprehend, classify message as postive or negative using sentimental analysis
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
            'date': date,
            'hour': hour,
            'username': username,
            'city': city,
            'state': state
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