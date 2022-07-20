import datetime
import time
import pytz


### Add the following code to the filter of submissions/comments ###

#0- # defining the timezone to UTC
tz = pytz.timezone("UTC")

#1- assign the desired date to a variable
start_time = tz.localize(datetime.datetime(2021, 7, 26, 21, 20)) # Year, month, day, hour, minute | # tz.localize is to set the UTC time zone  

# optional: print regular python date&time
print("date_time =>",start_time)
 
#2- convert datetime to unix and assign it to a variable
ux_start_time = int(time.mktime(start_time.timetuple()))

# optional: display unix timestamp after conversion
print("unix_timestamp => ",ux_start_time)
     
### Repeat the process for the date "before" | Short version: ###
end_time = tz.localize(datetime.datetime(2022, 7, 26, 21, 20)) 
ux_end_time = int(time.mktime(end_time.timetuple()))
  
#3- Include both variables as parameters in the filter 
