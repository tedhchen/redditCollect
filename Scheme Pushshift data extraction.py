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

## Extracting posts from the reddit "pushshift". Based on: https://github.com/Silvertongue26/reddit_api/blob/main/reddit6.py#L11

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

pd.set_option("display.max_columns", None)                  #Configuration for pandas to show all columns on dataframe
api = PushshiftAPI()                                        #We create an object of the API

def data_prep_posts(subreddit, start_time, end_time, filters, limit):
    if(len(filters) == 0):
        filters = ['id', 'author', 'created_utc',
                   'domain', 'url',
                   'title', 'num_comments']                 #We set by default some columns that will be useful for data analysis

    posts = list(api.search_submissions(
        subreddit="pushshift",                                #We set the subreddit we want to audit
        after=int(dt.datetime(2021, 1, 1).timestamp()),                                   #Start date
        before=int(dt.datetime(2021, 2, 1).timestamp()),                                   #End date
        filter=filters,                                     #Column names we want to get from reddit
        limit=limit))                                       #Max number of posts we wanto to recieve

    return pd.DataFrame(posts)                              #Return dataframe for analysis

###Function to plot the number of posts per day on the specified subreddit
def count_posts_per_date(df_p, title, xlabel, ylabel):
    df_p.groupby([df_p.datetime.dt.date]).count().plot(y='id', rot=45, kind='bar', label='Posts')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
