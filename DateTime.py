# Brandon Huschle _ VTF657
# CS5103 Final Project
# transform datetime string to different time zone\
# hh:mm:TZD  <- Military time : TZD = Time Zone Designator
# EX : 15:30:UTC

import sys

# Grab user input - split by :
userInput = sys.argv[1].split(":")
hour = int(userInput[0])
minute = int(userInput[1])
tzd = userInput[2]

# Test that information split properly
# print("hour " + hour + " minute " + minute + " TZD " + tzd)

# Convert to UTC

if (tzd == 'HST'):
    hour = hour + 10
elif (tzd == 'HDT'):
    hour = hour + 9
elif (tzd == 'AKDT'):
    hour = hour + 8
elif (tzd == 'PDT'):
    hour = hour + 7
elif (tzd == 'MST'):
    hour = hour + 7
elif (tzd == 'CDT'):
    hour = hour + 5
elif (tzd == 'EDT'):
    hour = hour + 4
else:
    print("You have not entered a valid TZD")
    sys.exit()

# Grab wanted new TZD
newTZD = sys.argv[2]

# Convert original tzd to new tzd
if (newTZD == 'HST'):
    hour = hour - 10
elif (newTZD == 'HDT'):
    hour = hour - 9
elif (newTZD == 'AKDT'):
    hour = hour - 8
elif (newTZD == 'PDT'):
    hour = hour - 7
elif (newTZD == 'MST'):
    hour = hour - 7
elif (newTZD == 'CDT'):
    hour = hour - 5
elif (newTZD == 'EDT'):
    hour = hour - 4
elif (newTZD == 'UTC'):
    hour = hour
else:
    print("You have not entered a valid TZD")
    sys.exit()


# print out new time for User
print(hour , ":" , minute , ":" , newTZD)