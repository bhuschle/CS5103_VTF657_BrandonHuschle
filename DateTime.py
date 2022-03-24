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
# print(month, day, year, hour, minute, tzd)

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


# initialize new variables for month, day, year
newMonth = month
newDay = day
newYear = year

# check that the month has not changed
thirtyOne = [1, 3, 5, 7, 8, 10, 12]
if (newMonth in thirtyOne and newDay > 31):
    if (newMonth != 12):
        newDay -= 31
        newMonth += 1
    else:
        newDay -= 31
        newMonth = 1
        newYear += 1
elif (newMonth == 2 and newDay > 28):
    newDay -= 28
    newMonth += 1
else:
    if (newDay > 30):
        newDay -= 30
        newMonth += 1
        

# convert days under 10 to strings so they have the 0 in front of them

if (newDay < 10):
    if (newDay == 1):
        newDay = '01'
    elif (newDay == 2):
        newDay = '02'
    elif (newDay == 2):
        newDay = '03'
    elif (newDay == 2):
        newDay = '04'
    elif (newDay == 2):
        newDay = '05'
    elif (newDay == 2):
        newDay = '06'
    elif (newDay == 2):
        newDay = '07'
    elif (newDay == 2):
        newDay = '08'
    elif (newDay == 2):
        newDay = '09'

# check hour and minute to see if date will have changed
if (newHour == 24):
    newHour = '00'
    newDay = day + 1
elif (newHour > 24):
    newHour = newHour - 24
    newDay = day + 1

# convert hours under 10 to strings so they have the 0 in front of them
if (newHour != '00' and newHour < 10):
    if (newHour == 1):
        newHour = '01'
    elif (newHour == 2):
        newHour = '02'
    elif (newHour == 2):
        newHour = '03'
    elif (newHour == 2):
        newDay = '04'
    elif (newHour == 2):
        newDay = '05'
    elif (newHour == 2):
        newHour = '06'
    elif (newHour == 2):
        newHour = '07'
    elif (newHour == 2):
        newHour = '08'
    elif (newHour == 2):
        newHour = '09'

# calculate date and time to see if it is daylight savings time
# if so then change time during UTC before switching to new TZD

# print out new time for User
print(newMonth, newDay, newYear)
print(newHour , ":" , minute , ":" , newTZD)