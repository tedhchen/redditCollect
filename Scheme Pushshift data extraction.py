## Main steps to extract reddit data via Pushshift ##
"""
Logic of the code:
1. download all reddit data 
2. verify that the desired data is the same as the one extracted using filters (parameters)
3. If the data looks the same, proceed to identify the elements with missing values (pics, gifs, videos)
4. Use PRAW to collect the missing values and merge them with the original database (using the SubId)


Next steps:
- Figure out how to download all Reddit data
- Explore whether the data formats for datasets exctracted using PRAW are similar/same to those using Pushshift (e.g. same columns?) 
- Sketch the main functions 
"""

pip install pmaw pandas
import pandas as pd
from pmaw import PushshiftAPIapi = PushshiftAPI()

