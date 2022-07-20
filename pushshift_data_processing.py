#Note: for this code, we need to decompress and run the code for every monthly file separately
    #Is there a better way to decompress and run selected monthly files at once?
    
#Note: Reddit data uses unix timestamps, creation time of each item is UTC
    #This code uses UTC timestamp for timeperiod filtering

import json
import pandas as pd

#Open the submission file
submissions = []
for line in open('filename.json'):
    submissions.append(json.loads(line))

#Use list comprehension to retrieve submissions that fulfill conditions

#Filter for timeperiod
#Define start_time and end_time for wanted timeperiod to collect data within a timerange
start_time = pytz.timezone('UTC').localize(datetime.datetime(2000, 01, 01, 0, 0, 0)) #Year, month, day, hour, minute | # tz.localize is to set the UTC time zone
end_time = pytz.timezone('UTC').localize(datetime.datetime(2001, 01, 01, 0, 0, 0))  #Year, month, day, hour, minute | # tz.localize is to set the UTC time zone

ux_start_time = int(time.mktime(start_time.timetuple())) #Convert datetime to unix
ux_end_time = int(time.mktime(end_time.timetuple())) #Convert datetime to unix

submissions = [time for time in submissions if time['created_utc'] in range(ux_start_time,ux_end_time)] #filter items

#column equals condition: filter for retrieving items, where key equals wanted value
#can be used to retrieve submissions from any subreddits, any authors etc.
valuelist = ['value1', 'value2'] #define wanted values
submissions = [value for value in submissions if value['key'] in valuelist] #filter items

#key includes searchword
#can be used to retrieve submissions where title or selftext includes searchwords
submissions = [value for value in submissions if 'searchword1' in value['key'].lower() or 'searchword2' in value['key'].lower() and 'searchword3' in value['key'].lower()] #filter items

#Format the filtered list of submissions as a dataframe
df_rs = pd.DataFrame(submissions)
df_rs.head()

#Filter comments

#Open comment file
comments = []
for line in open('filename.json'):
    comments.append(json.loads(line))
    
#Use list comprehension to retrieve comments, where link_id is equal to any id of selected submissions
link_id_list = df['id'].tolist() #define set of link_ids
comments = [value for value in comments if value['link_id'] in link_id_list] #filter items

#Format the filtered list of comments as a dataframe
df_rc = pd.DataFrame(comments)
df_rc.head()

#Saving comments and submissions separately
df_rs.to_csv('RS_set_year_month.csv')
df_rc.to_csv('RC_set_year_month.csv')

#Combining comments and submissions
df_rs['type'] = 'submission'   #Add a type column to indicate item type (comment or submission)
df_rc['type'] = 'comment'     #Add a type column to indicate item type (comment or submission)

df_rs.rename(columns = {'id':'link_id'}, inplace = True)   #Unify headers of overlapping id column

reddit_data = pd.concat([df_rs, df_rc])   #Concenate comments and submissions

#Note: Add function to group data by link_id
#Note: Check that data is in chronological order

reddit_data.to_csv('REDDIT_set_dates.csv')

#Note: post_hint column seems to have 'image' as value if the post contains a photo
#Note: The column link_id would allow us to match comments with submission. Link: https://galenweld.github.io/reddit_join_comments_example/
