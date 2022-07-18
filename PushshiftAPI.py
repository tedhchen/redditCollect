import psaw
from psaw import PushshiftAPI
import pandas as pd

api = PushshiftAPI()

posts = list(api.search_submissions(
        subreddit='stamps', limit = 10))

df = pd.DataFrame([thing.d_ for thing in posts])

print(df)

df.to_csv('filename.csv')
