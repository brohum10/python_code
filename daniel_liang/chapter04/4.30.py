GMT = eval(input("Enter the time zone offset to GMT: "))

import time

currentTime = time.time() # Get curremt time

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

#Get the current seconds
currentSecond = totalSeconds % 60

#Obtain the total minutes
totalMinutes = totalSeconds // 60

#Compute the current minute in the hour
currentMinute = totalMinutes % 60

#Obtain the total hours
totalHours = totalMinutes // 60

#Compute the current hour plus GMT
currentHour = (totalHours % 24) + GMT
currentHour = currentHour-12
print("Current time is", currentHour, ":", currentMinute, ":", currentSecond, "GMT")
