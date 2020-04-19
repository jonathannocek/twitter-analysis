import boto3
import base64
import json
import time

# These packages needs to be added as layers to Lambda:
import geopy


def lambda_handler(event, context):

    output = []  # Initialize output list
    for record in event["records"]:
        # Coded in base64, Retrieve data
        tweet = base64.b64decode(record["data"]).decode("utf-8").strip()
        text = json.loads(tweet)["text"]
        username = json.loads(tweet)["user"]["screen_name"]

        # Format datetime so Kibana reads it
        created_at = json.loads(tweet)["created_at"]
        datetime = time.strftime(
            "%Y-%m-%dT%H:%M:%S", time.strptime(created_at, "%a %b %d %H:%M:%S +0000 %Y")
        )

        # Get city, state
        place_raw = json.loads(tweet)["place"]["full_name"]
        place = [x.strip() for x in place_raw.split(", ")]
        city = place[0]
        state = place[1]

        # Using geopy to determine lat/long based on city, state
        locator = geopy.Nominatim(user_agent="myGeocode")
        location = locator.geocode(place_raw)
        latitude = location.latitude
        longitude = location.longitude

        # Using AWS Comprehend, classify message as postive or negative using sentimental analysis
        comprehend = boto3.client(service_name="comprehend", region_name="us-east-1")
        sentiment = comprehend.detect_sentiment(Text=text, LanguageCode="en")
        s = sentiment["Sentiment"]
        print(s)

        # Using AWS Comprehend, detect key phrases
        phrases = comprehend.detect_key_phrases(Text=text, LanguageCode="en")
        p = phrases["KeyPhrases"]
        print(p)

        # Retrieve positive, negative scores. Subtract to find total score
        positive = sentiment["SentimentScore"]["Positive"]
        negative = sentiment["SentimentScore"]["Negative"]
        score = positive - negative
        print(score)

        data_record = {
            "text": text,
            "sentiment": s,
            "score": score,
            "phrases": p,
            "datetime": datetime,
            "username": username,
            "place": {"city": city, "state": state,},
            "location": [longitude, latitude],
        }
        print(data_record)

        output_record = {
            "recordId": record["recordId"],
            "result": "Ok",
            "data": base64.b64encode(json.dumps(data_record).encode("utf-8")).decode(
                "utf-8"
            ),
        }
        print(output_record)
        output.append(output_record)

    print(output)
    return {"records": output}
