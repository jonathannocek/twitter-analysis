import TwitterSearch
import credentials
import geopy
import time
import os

def search(query):
    try:
        tso = TwitterSearch.TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords(['Elon Musk']) # let's define all words we would like to have a look for
        tso.set_language('en') # we want to see English tweets only
        tso.set_include_entities(False) # and don't give us all those entity information

        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch.TwitterSearch(
            consumer_key = credentials.consumer_key,
            consumer_secret = credentials.consumer_secret,
            access_token = credentials.access_token,
            access_token_secret = credentials.access_token_secret
        )

        # this is where the fun actually starts :)
        for tweet in ts.search_tweets_iterable(tso):
            text = tweet['text']
            username = tweet["user"]["screen_name"]
            # Format datetime so Kibana reads it
            created_at = tweet["created_at"] 
            datetime = time.strftime('%Y-%m-%dT%H:%M:%S', time.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y'))

            # Get city, state
            place_raw = tweet['place']['full_name']
            place = [x.strip() for x in place_raw.split(', ')]
            city = place[0]
            state = place[1]

            # Using geopy to determine lat/long based on city, state
            locator = geopy.Nominatim(user_agent ='myGeocode')
            location = locator.geocode(place_raw)
            latitude = location.latitude
            longitude = location.longitude

            data_record = {
            'text': text,
            'datetime': datetime,
            'username': username,
            'place' : {
                'city': city,
                'state': state,
            },
            'location' : [longitude,latitude]
        }


    except TwitterSearch.TwitterSearchException as e: 
        print(e)