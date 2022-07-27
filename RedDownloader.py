""" RedDownloader facilitates the download of images, videos, gifs and gallery posts of selected Reddit submissions (based on the submission's "permalink")
This code downloades the media in chronological order (the first downloaded image corresponds to the first link of the list). 

Steps for using the code:
 1. pip install RedDownloader
 2. Create a destination folder for the media and add it as "path" (line 17)
 3. Extract the links of the submissions that contain images/videos/gifs: 
    3.1 The links are found in the column "permalink" of the main dataset
    3.2 Submissions with media can be identified by the value "XXX" in the column "XXX" 
4. Add the selected links to the list "yes_media".
5. Define the desired quality for the media according to memory availability (line 17)  
"""
 

from RedDownloader import RedDownloader
yes_media = ["List with the permalinks of submissions with media"] 
for url in yes_media: RedDownloader.Download(yes_media, destination="path", quality=480) # Define quality: 144, 240, 360, 480, 720, 1080 
