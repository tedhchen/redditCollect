import psaw
from psaw import PushshiftAPI
import pandas as pd

api = PushshiftAPI()

posts = list(api.search_submissions(
        subreddit='stamps', limit = 10))

df = pd.DataFrame([thing.d_ for thing in posts])

print(df)

df.to_csv('filename.csv')


#Note: post_hint column seems to have 'image' as value if the post contains a photo
