# Presentation 2: Week of January 26th

## Current State

This week, I was able to do some additional data cleaning on the initial json file. Now, I am passing the
following variables into Kibana: username, tweet, city, state, sentiment, datatime, score. I was able to stream
tweets containing 'Trump' and learned that there were approximately 10 tweets per 30 seconds on Friday night. 

![Kibana Example](../images/kibana-example1.png)

## System Design

![System Design as of 02-03-2020](../images/presentation-two.jpg)


## Research Question

How popular are the 2020 Presidential candidates on Twitter?
- So far I have been only streaming for tweets containing 'Trump'

![Popularity as of 02-03-2020](../images/popularity_02_03_2020.png)

## Potential Exploration

- Map city, state to latitude/longitude coords so it can be used via a map
- Divide the streaming data by state and determine difference
- Use state data to do logsitic regression to determine red/blue state
- Potentially use old data from 2016 Presidential Election to train new model