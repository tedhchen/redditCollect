import psaw
from psaw import PushshiftAPI

api = PushshiftAPI()

posts = list(api.search_submissions(
        subreddit='stamps', limit = 10))

df = pd.DataFrame(posts)

print(df)

df.to_csv('filename.csv')
