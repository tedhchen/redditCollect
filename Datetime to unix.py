import datetime
import time
import pytz


### Add the following code to the filter of submissions/comments ###

#0- # defining the timezone to UTC
tz = pytz.timezone("UTC")

#1- assign the desired date to a variable

date_time_after = tz.localize(datetime.datetime(2021, 7, 26, 21, 20)) # Year, month, day, hour, minute | # tz.localize is to set the UTC time zone  

# optional: print regular python date&time
print("date_time =>",date_time_after)
 
#2- convert datetime to unix and assign it to a variable
unix_time_after = int(time.mktime(date_time_after.timetuple()))

  
# optional: display unix timestamp after conversion
print("unix_timestamp => ",unix_time_after)
     
  
### Repeat the process for the date "before" | Short version: ###
date_time_before = tz.localize(datetime.datetime(2022, 7, 26, 21, 20)) 
unix_time_before = int(time.mktime(date_time_before.timetuple()))

  
  
#3- Include both variables as parameters in the filter 