## Main steps to extract reddit data via Pushshift ##
"""
Logic of the code:
1. download all reddit data 
2. verify that the desired data is the same as the one extracted using filters (parameters)
3. If the data looks the same, proceed to identify the elements with missing values (pics, gifs, videos)
4. Use PRAW to collect the missing values and merge them with the original database (using the SubId)


Next steps:
- Figure out how to download all Reddit data
- Explore whether the data formats for datasets exctracted using PRAW are similar/same to those using Pushshift (e.g. same columns?) 
- Sketch the main functions 
"""

##  Based on: https://github.com/Silvertongue26/reddit_api/blob/main/reddit6.py#L11
# Load packages
import pandas as pd
import requests
import json
import datetime
import csv
import psaw
from psaw import PushshiftAPI                               #Importing wrapper library for reddit(Pushshift)
import datetime as dt                                       #Importing library for date management
import pandas as pd                                         #Importing library for data manipulation in python
import matplotlib.pyplot as plt                             #Importing library for creating interactive visualizations in Python
from pprint import pprint

### Extract submissions from a specific subreddit

    import psaw
from psaw import PushshiftAPI
import pandas as pd

api = PushshiftAPI()

api_request_generator = list(api.search_submissions(
        subreddit='stamps', limit = 100))

submissions = pd.DataFrame([submission.d_ for submission in api_request_generator])

print(submissions.columns)


## Extracting comments within a specific subreddit

api_request_generator = list(api.search_comments(
        subreddit='stamps', limit = 100))

comments = pd.DataFrame([comments.d_ for comments in api_request_generator])

print(comments.columns)
""""""

#Sonjas way
submissions.rename(columns = {'id':'link_id'}, inplace = True)

comments_and_submissions = pd.concat([submissions, comments])

comment_and_submissions.head()
#Sonjas way


# Joining the comments to the submissions

grouped_comments = comments.groupby('link_id').agg({'body': '\n'.join})
grouped_comments

print(grouped_comments.head(5))

df = submissions.set_index('id').join(grouped_comments).astype(str)
print(df)

print(df.columns)

df['text'] = df[['title', 'selftext', 'body']].agg('\n'.join, axis='columns')
df

path=r"C:\Users\ricoe\df.csv', index = False)"
df.to_csv(path)

x = pd.read_csv(r"C:\Users\ricoe\df.csv")

x.head(20)
