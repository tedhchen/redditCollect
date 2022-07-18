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

#Columns:
"""
'all_awardings', 'allow_live_comments', 'author',
       'author_flair_background_color', 'author_flair_css_class',
       'author_flair_richtext', 'author_flair_template_id',
       'author_flair_text', 'author_flair_text_color', 'author_flair_type',
       'author_fullname', 'author_is_blocked', 'author_patreon_flair',
       'author_premium', 'awarders', 'can_mod_post', 'contest_mode',
       'created_utc', 'domain', 'full_link', 'gildings', 'id',
       'is_created_from_ads_ui', 'is_crosspostable', 'is_meta',
       'is_original_content', 'is_reddit_media_domain', 'is_robot_indexable',
       'is_self', 'is_video', 'link_flair_background_color',
       'link_flair_richtext', 'link_flair_template_id', 'link_flair_text',
       'link_flair_text_color', 'link_flair_type', 'locked', 'media_only',
       'no_follow', 'num_comments', 'num_crossposts', 'over_18', 'permalink',
       'pinned', 'post_hint', 'preview', 'retrieved_on', 'score', 'selftext',
       'send_replies', 'spoiler', 'stickied', 'subreddit', 'subreddit_id',
       'subreddit_subscribers', 'subreddit_type', 'suggested_sort',
       'thumbnail', 'thumbnail_height', 'thumbnail_width', 'title',
       'total_awards_received', 'treatment_tags', 'upvote_ratio', 'url',
       'url_overridden_by_dest', 'created', 'parent_whitelist_status', 'pwls',
       'whitelist_status', 'wls', 'media', 'media_embed',
       'removed_by_category', 'secure_media', 'secure_media_embed',
       'gallery_data', 'is_gallery', 'media_metadata', 'crosspost_parent',
       'crosspost_parent_list'],
      dtype='object')
      """

""" How to merge submissions and comments: https://galenweld.github.io/reddit_join_comments_example/
