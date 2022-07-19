import json
import pandas as pd

#Open the submission file
submissions = []
for line in open('filename.json'):
    submissions.append(json.loads(line))

#Use list comprehension to retrieve submissions that fulfill conditions

#column equals condition: filter for retrieving items, where key equals wanted value
#can be used to retrieve submissions from any subreddits, any authors etc.
valuelist = ['value1', 'value2'] #define wanted values
submissions = [value for value in submissions if value['key'] in valuelist] #filter items

#key includes searchword
#can be used to retrieve submissions where title or selftext includes searchwords
submissions = [value for value in submissions if 'searchword1' in value['key'].lower() or 'searchword2' in value['key'].lower() and 'searchword3' in value['key'].lower()] #filter items

#Format the filtered list as a dataframe
df = pd.DataFrame(submissions)
df.head()

#Note: post_hint column seems to have 'image' as value if the post contains a photo
#Note: The column link_id would allow us to match comments with submission. Link: https://galenweld.github.io/reddit_join_comments_example/
