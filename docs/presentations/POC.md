# Twitter Analysis: Proof of Concept

## Background

This is a project for DS395 at Illinois Wesleyan University. This course finishes the Data Science minor by having students
do a independent study Capstone project that will be presented via a poster at the John Wesley Powell conference at the end
of the semester. As a Computer Science major, I want to focus on all aspects of Data Science. This includes the capturing,
cleaning, curating, and analysis of the data. I also have interest in Cloud Computing and intend to include this in my project
in order to improve my skills and learn how Data Science can be done on the Cloud.

## Idea

My idea for this project is to utilize the Twitter API to stream tweets in realtime and come to conclusions about what is
happening now. One idea that I have to look into how popular political figures are percieved and how this could change throughout
time as different news breaks. For example, I would like to see people's general reactions when Donald Trump tweets or about
different candidates during the 2020 Democratic debates and primaries. 

## Process

After doing research about the possible solutions for my idea, I intend to use the various services from Amazon Web Services 
to solve my problem. Here is the general flow of data that I propose:
- Data Collection: Twitter API via Tweepy 
- Data Ingestion: AWS Kinesis Firehose
- Data Cleaning/Curation: AWS Lambda inside Kinesis Firehose
- Data Analysis: Sentimental Analysis via AWS Comprehend
- Data Storage: Elasticsearch
- Data Visualization: Kibana Dashboard