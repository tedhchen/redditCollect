# Reddit data extraction tool 

This repository contains code to collect data from Reddit. It enables the filtering and extraction of selected data based on the researcher's interests. For example, it facilitates the search and download of data corresponding to a specific time period, or within a selected Subreddit, or including certain keywords. Over 12 different parameters allow for a highly customizable search. 

The repository includes three files:

pushshift_data_processing.py -> the main code

RedDownloader.py -> code for downloading media resources from posts

Decompress zstd -> instructions for decompressing the raw data

# Before using the code
Before thinking what parameters (filters) should be adapted to obtain relevant data, it's key to know the following:
1. The code can (so far) only extract data specific to one calendar month. 

2. The code can (so far) only carry out searches of submissions, not of comments. Based on the extracted submissions, the code finds the comments within those submissions and merges them with the respective submissions into a single csv file (using a unique ID). 

3. The raw data has to be accessed, selected, downloaded and decompressed before running the code. For that:

    2.1. Enter https://files.pushshift.io/reddit/
   
    2.2. Click on submissions -> download the desired month
    
    2.3. Go back and click on comments -> download the desired month

    2.4 Decompress the files and save them. Follow these steps to decompress the file:
    
       # Install zstandard: https://sourceforge.net/projects/zstd-for-windows/files/latest/download
         zstd -d ("name of the file-submissions") --long=31  # decompress the submissions file
         zstd -d ("name of the file-comments") --long=31  # decompress the comments file



# Using the code 
Do a brainstorming of the information you'd like to get. Is it one specific Subreddit that you'd like to explore, or all posts/comments using one or multiple keywords? After that, customize the code by adding and apapting the parameters as you consider convenient. For a list of all customizable parameters, access the API documentation: https://github.com/pushshift/api/blob/master/README.md
 
Open the main code: file pushshift_data_processing.py.

In principle, the only lines that have to be adapted (besides the file paths) are: [ADD THE LINES NUMBER WHEN AVAILABLE] 

Once this is done, run the code and open the created csv to confirm the extraction was sucessfull.

# Understanding the output
The CSV will have the following columns: 
(ofs means only available for submissions)
(ofc means only available for comments)

'archived': ofs

-> 'author': User nickname

'author_flair_background_color':

'author_flair_css_class':

'author_flair_richtext':

'author_flair_text':

'author_flair_text_color': 

'author_flair_type':

'brand_safe': ofs

'can_gild': ofs

'contest_mode': ofs

-> 'created_utc': time when the content was posted (UTC)

'distinguished':

'domain': ofs

-> 'edited': whether the content has been edited

'gilded': 

'hidden': ofs

'hide_score': ofs

'link_id': link ID

'is_crosspostable':

'is_reddit_media_domain': 

'is_self': 

'is_video',

'link_flair_css_class', 

'link_flair_richtext', 

'link_flair_text', 

'link_flair_text_color', 

'link_flair_type', 

'locked', 

'media',

'media_embed',

'no_follow', 

'num_comments', 

'num_crossposts', 

'over_18', 

'parent_whitelist_status', 

-> 'permalink': permanent link to the comment

'retrieved_on': date when the data was extracted (UTC)

'rte_mode', 

'score', 

'secure_media',

'secure_media_embed',

'selftext',

'send_replies',

'spoiler',

'stickied', 

-> 'subreddit': Subreddit (?)

'subreddit_id',

'subreddit_name_prefixed', 

'subreddit_type', 

'suggested_sort',

'thumbnail', 

'thumbnail_height',

'thumbnail_width', 

-> 'title': ofs Title

'url': ofs (?)

'whitelist_status', 

'post_hint', 

'preview',

-> 'type': submission or comment?

'controversiality', 

-> 'body': ofc Comments separated by line spacing

'ups', 

'id', 

'parent_id'], 

dtype='object'


# Downloading multimedia resources posted in submissions
The code found in pushshift_data_processing.py doesn't extract images/videos/gifs/gallery posts. If you'd like to explore those resources, please read the instructions and use the code in the file RedDownloader.py (after you have run the main code).

# Background information
The code makes use of two data sources:
1. Pushshift - a non-official server saving all Reddit data by month(data divided into submissions & comments) -> https://files.pushshift.io.
2. The official Reddit API (only complementarily to replace missing values) -> Python Reddit API Wrapper (PRAW)
