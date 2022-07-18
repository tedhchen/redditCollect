import psaw
from psaw import PushshiftAPI
import pandas as pd

#Initialize pushshift
api = PushshiftAPI()

#Define api_request_generator and establish the parameters of the query
#Full list of parameters: https://pushshift.io/api-parameters/
api_request_generator = list(api.search_submissions(
        subreddit='title', limit = 10))

#Organize data into dataframe
submissions = pd.DataFrame([submission.d_ for submission in api_request_generator])

#Check to see what columns/metadata exist in this data
submissions.columns

print(submissions)

submissions.to_csv('filename.csv')


#Note: post_hint column seems to have 'image' as value if the post contains a photo


