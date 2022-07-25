# Reddit data extraction tool 

# Preface
This repository contains code to collect data from Reddit. It enables the filtering and extraction of selected data based on the researcher's interests. For example, it facilitates the search and download of data corresponding to a specific time period, or within a selected Subreddit, or including certain keywords. Over 12 different parameters allow for a highly customizable search. 

# Before using the code
Before thinking what parameters (filters) should be adapted to obtain relevant data, it's key to know the following:
1. The code can (so far) only extract data specific to one calendar month. 
2. The data has to be accessed, selected, downloaded and decompressed before running the code. For that:
    2.1. Enter https://files.pushshift.io/reddit/
    2.2. Click on submissions -> download the desired month
    2.3. Go back and click on comments -> download the desired month

# Using the code 
Do a brainstorming of the information you'd like to get. Is it one specific Subreddit that you'd like to explore, or all posts/comments using one or multiple keywords? After that, customize the code by adding and apapting the parameters as you consider convenient. For a list of all customizable parameters access the API documentation: https://github.com/pushshift/api/blob/master/README.md
 
The lines that should be adapted are: [ ] 

Once this is done, run the code and open the created csv to confirm the extraction was sucessfull.


# Maybe relevant
The code makes use of two data sources:
1. Pushshift - a non-official server saving all Reddit data by month(data divided into submissions & comments) -> https://files.pushshift.io.
2. The official Reddit API (only complementarily to replace missing values) -> Python Reddit API Wrapper (PRAW)






]

