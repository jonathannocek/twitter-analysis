# Presentation One

Present research question, data descriptives, analyses or planned analyses.

## Overview

## Research Questions

What is Donald Trump's and potential Democratic nominees' (Joe Biden, Bernie Sanders, etc.) popularity on Twitter?
- How does this popularity change with current events? (debates, tweets, impeachment trial, etc.)
- Can we break this down to the state level?
- If we can break this down to the state level, can we classify how a state will vote based on the sentimental analysis?

## Process 

1. Data Collection: Twitter API via Tweepy 
2. Data Ingestion: AWS Kinesis Firehose
3. Data Cleaning/Curation: AWS Lambda inside Kinesis Firehose
4. Data Analysis: Sentimental Analysis via AWS Comprehend
5. Data Storage: Elasticsearch
6. Data Visualization: Kibana Dashboard

## Architecture

![Week One Architecture](../images/presentation-one.jpg)

### Raw Data

The following is an example of the raw data after using the Twitter API

```
{"created_at":"Tue Jan 14 12:44:41 +0000 2020","id":1217064995114180608,"id_str":"1217064995114180608","text":"Mitt Romney makes Jeff Flake look like Ronald Reagan. He\u2019s a back-stabbing coward who\u2019s bitter because he blew one\u2026 https:\/\/t.co\/dOZAgzSK56","source":"\u003ca href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\"\u003eTwitter for iPhone\u003c\/a\u003e","truncated":true,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":232901331,"id_str":"232901331","name":"Dan Bongino","screen_name":"dbongino","location":"Florida, USA","url":"http:\/\/www.bongino.com","description":"Host of The Dan Bongino Show.","translator_type":"none","protected":false,"verified":true,"followers_count":1398949,"friends_count":654,"listed_count":4730,"favourites_count":56592,"statuses_count":57099,"created_at":"Sat Jan 01 17:50:03 +0000 2011","utc_offset":null,"time_zone":null,"geo_enabled":true,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"FFFFFF","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":false,"profile_link_color":"0084B4","profile_sidebar_border_color":"FFFFFF","profile_sidebar_fill_color":"C0DFEC","profile_text_color":"333333","profile_use_background_image":false,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1085298427662077952\/G7pyO36A_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1085298427662077952\/G7pyO36A_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/232901331\/1548899037","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"extended_tweet":{"full_text":"Mitt Romney makes Jeff Flake look like Ronald Reagan. He\u2019s a back-stabbing coward who\u2019s bitter because he blew one of the most winnable elections in American history and Donald Trump had to clean up his mess.","display_text_range":[0,208],"entities":{"hashtags":[],"urls":[],"user_mentions":[],"symbols":[]}},"quote_count":464,"reply_count":1096,"retweet_count":8690,"favorite_count":30358,"entities":{"hashtags":[],"urls":[{"url":"https:\/\/t.co\/dOZAgzSK56","expanded_url":"https:\/\/twitter.com\/i\/web\/status\/1217064995114180608","display_url":"twitter.com\/i\/web\/status\/1\u2026","indices":[116,139]}],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"en"},"quoted_status_permalink":{"url":"https:\/\/t.co\/nZUQR6p0Zw","expanded":"https:\/\/twitter.com\/dbongino\/status\/1217064995114180608","display":"twitter.com\/dbongino\/statu\u2026"},"is_quote_status":true,"extended_tweet":{"full_text":"Just another self absorbed rich dud (left the e off deliberately) with an over blown opinion with regard for his mental faculties!","display_text_range":[0,130],"entities":{"hashtags":[],"urls":[],"user_mentions":[],"symbols":[]}},"quote_count":0,"reply_count":0,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[{"url":"https:\/\/t.co\/w7TuD7jrQf","expanded_url":"https:\/\/twitter.com\/i\/web\/status\/1217122470764908545","display_url":"twitter.com\/i\/web\/status\/1\u2026","indices":[117,140]}],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"en","timestamp_ms":"1579019584729"}
```

### After Some Cleaning

The following is an example of the data after curation and sentimental analysis in the form of a json file

```
    {
        "message": "Donald Trump wants his impeachment trial to end before his state of the union address in just two weeks’ time, Lind… https://t.co/rwbiWYglRT",
        "sentiment": "NEUTRAL",
        "total": -0.09744752780534327
    },
    {
        "message": "@realDonaldTrump Best President ever President Donald J Trump.",
        "sentiment": "POSITIVE",
        "total": 0.8768189063412137
    },
    {
        "message": "Republicans know full well trump is guilty. They swore an oath and immediately broke it.",
        "sentiment": "NEGATIVE",
        "total": -0.862764734774828
    },
```
