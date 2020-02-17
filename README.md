# Twitter Analysis: Creating a real-time data pipeline to analyze tweets

Author: Jonathan Nocek

## Overview

This project aims to provide real time information from Twitter about what is happening now. Through Tweepy and various services from Amazon Web Services, tweets are streamed, sent through a data pipeline, and finally visualized using a Kibana dashboard. 

## Background

This is a project for DS395 at Illinois Wesleyan University during the 2020 Spring semester. This course finishes the Data Science minor by having students do a independent study Capstone project that will be presented during the John Wesley Powell conference at the end of the semester. This project aims to provide analysis around the 2020 Democratic primaries and General Election.

## Design

![Design](docs/images/presentation-two.jpg)

## Technology

- Tweepy: A python wrapper for the Twitter API
- AWS EC2: Web service that provides cloud computing from Amazon Web Services
- AWS Kinesis Firehose: Prepares and loads real-time streams into various data stores and analytics tools
- AWS Lambda: Serverless compute
- AWS Comprehend: Natural Language Processing (NLP) services that uses machine learning to find insights and relationships in text
- Amazon Elasticsearch service: Fully managed service that deploys, secures, and runs Elasticsearch
- Kibana: Open source analytics and visualizations platform designed to work with Elasticsearch

## Kibana Examples

![Kibana Dashboard](docs/images/kibana_example_1.png)

![Kibana Dashboard](docs/images/kibana_example_2.png)

![Kibana Link](https://search-twitter-elasticsearch-hcicwk5gfmpfqsfxpehilnn2fa.us-east-1.es.amazonaws.com/_plugin/kibana/)

## Author

- Jonathan Nocek - *jnocek@iwu.edu*


