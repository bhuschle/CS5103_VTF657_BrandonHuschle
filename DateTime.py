# Brandon Huschle _ VTF657
# CS5103 Final Project
# transform datetime string to different time zone
# add information needed for calculating daylight savings time
# mm:dd:yyyy:hh:mm:TZD  <- month:day:year:Military time : TZD = Time Zone Designator
# EX : 12:21:2022:15:30:UTC

import sys

# Grab user input - split by :
userInput = sys.argv[1].split(":")
month = int(userInput[0])
day = int(userInput[1])
year = int(userInput[2])
hour = int(userInput[3])
minute = int(userInput[4])
tzd = userInput[5]

# Test that information split properly
# print("hour " + hour + " minute " + minute + " TZD " + tzd)

# Convert to UTC

if (tzd == 'HST'):
    newHour = hour + 10
elif (tzd == 'HDT'):
    newHour = hour + 9
elif (tzd == 'AKDT'):
    newHour = hour + 8
elif (tzd == 'PDT'):
    newHour = hour + 7
elif (tzd == 'MST'):
    newHour = hour + 7
elif (tzd == 'CDT'):
    newHour = hour + 5
elif (tzd == 'EDT'):
    newHour = hour + 4
else:
    print("You have not entered a valid TZD")
    sys.exit()

# Grab wanted new TZD
newTZD = sys.argv[2]

# Convert UTC to new tzd
if (newTZD == 'HST'):
    newHour = newHour - 10
elif (newTZD == 'HDT'):
    newHour = newHour - 9
elif (newTZD == 'AKDT'):
    newHour = newHour - 8
elif (newTZD == 'PDT'):
    newHour = newHour - 7
elif (newTZD == 'MST'):
    newHour = newHour - 7
elif (newTZD == 'CDT'):
    newHour = newHour - 5
elif (newTZD == 'EDT'):
    newHour = newHour - 4
elif (newTZD == 'UTC'):
    newHour = newHour
else:
    print("You have not entered a valid TZD")
    sys.exit()

# print out new time for User
print(hour , ":" , minute , ":" , newTZD)