import datetime
import time
import pytz


### Add the following code to the filter of submissions/comments ###

#0- # defining the timezone to UTC
tz = pytz.timezone("UTC")

#1- assign the desired date to a variable
date_time_after = datetime.datetime(2021, 7, 26, 21, 20) # year, month, day, hour, minute
date_time_after = tz.localize(date_time_after) # Localizing the time zone to Helsinki 
 
# optional: print regular python date&time
print("date_time =>",date_time_after)
 
#2- convert datetime to unix and assign it to a variable
unix_time_after = time.mktime(date_time_after.timetuple())
unix_time_after = int(unix_time_after)
  
# optional: display unix timestamp after conversion
print("unix_timestamp => ",unix_time_after)
     
  
### Repeat the process for the date "before" | Short version: ###
date_time_before = datetime.datetime(2022, 6, 26, 21, 20) 
date_time_before = tz.localize(date_time_before) 
unix_time_before = time.mktime(date_time_before.timetuple())
unix_time_before = int(unix_time_before)
  
  
#3- Include both variables as parameters in the filter 
