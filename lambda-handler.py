import boto3
import base64
import json

def lambda_handler(event, context):
    output = []

    for record in event['records']:
        
        # Coded in base64, Retrieve message
        message = base64.b64decode(record['data']).decode('utf-8').strip()
        print(message)

        # Using AWS Comprehend, classify message as postive or negative
        comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
        sentiment_all = comprehend.detect_sentiment(Text=message, LanguageCode='en')
        sentiment = sentiment_all['Sentiment']
        print(sentiment)
        positive = sentiment_all['SentimentScore']['Positive']
        negative = sentiment_all['SentimentScore']['Negative']
        total = positive - negative
        print(total)
        
        data_record = {
            'message': message,
            'sentiment': sentiment,
            'total': total
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