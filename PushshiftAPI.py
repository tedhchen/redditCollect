import psaw
from psaw import PushshiftAPI

api = PushshiftAPI()

posts = list(api.search_submissions(
        subreddit='stamps', limit = 10))

print(posts)
