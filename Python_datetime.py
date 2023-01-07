"""
This script is for telling weather 3 branches in three different timezones are open


"""

import datetime
import pytz


#currentDateAndTime = datetime.now()

#local_time = print("Local Time: {}:{}".format(currentDateAndTime.hour,currentDateAndTime.minute))
#print(local_time)

#zones = pytz.all_timezones
#print(zones)

### --- TIME ZONES --- ###

#currentDateAndTime = datetime.datetime.now()
#print("The local current time is: {}\n\nTimes Around The world:".format(currentDateAndTime.strftime("%H:%M")))


currentDateAndTime = datetime.datetime.now()
print("The local current time is: {}\n\nTimes Around The world:".format(currentDateAndTime.strftime("%H:%M")))

# this gets the time in New York
NewYorktz = pytz.timezone("America/New_York")
timeInNewYork = datetime.datetime.now(NewYorktz)
currentTimeInNewYork = timeInNewYork.strftime("%H:%M")
print("The Current Time in New York: {}".format(currentTimeInNewYork))

# This gets the time in London
Londontz = pytz.timezone("Europe/London")
timeInLondon = datetime.datetime.now(Londontz)
currentTimeInLondon = timeInLondon.strftime("%H:%M")
print("The Current Time in London: {}".format(currentTimeInLondon))

Portlandtz = pytz.timezone("America/Los_Angeles")
timeInPortland = datetime.datetime.now(Portlandtz)
currentTimeInPortland = timeInPortland.strftime("%H:%M")
print("The current time in Portland: {}".format(currentTimeInPortland))


#### ---- We are taking the strings(times) and converting them to integers ---- ####

#splits the string at the ":" then changes them to integers and readds them to the list
temp_list = currentTimeInPortland.split(":")
Portland_list = []

for item in temp_list:
    new_item = int(item)
    Portland_list.append(new_item)

# New York getting the same task done
temp_list = currentTimeInNewYork.split(":")
NewYork_list = []

for item in temp_list:
    new_item = int(item)
    NewYork_list.append(new_item)

# finally London
temp_list = currentTimeInLondon.split(":")
London_list = []

for item in temp_list:
    new_item = int(item)
    London_list.append(new_item)


#### --- Output --- ####
print("\n")
# For newyork
if 17 <= NewYork_list[0] > 9:
    print("New York Branch: closed")
else:
    print("New York Branch: Open")
# for portland
if 17 <= Portland_list[0] > 9:
    print("Portland Branch: closed")
else:
    print("Portland Branch: Open")

# for London
if 17 <= London_list[0] > 9:
    print("London Branch: closed")
else:
    print("London Branch: Open")
