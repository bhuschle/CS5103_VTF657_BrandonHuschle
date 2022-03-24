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
    if (newMonth == 12):
        newDay = newDay - 31
        newMonth = 1
        newYear = newYear + 1
    else:
        newDay = newDay - 31
        newMonth = newMonth + 1
elif (newMonth == 2 and newDay > 28):
    newDay = newDay - 28
    newMonth = newMonth + 1
else:
    if (newDay > 30):
        newDay = newDay - 30
        newMonth = newMonth + 1

# check daylight savings time to see if hour needs to be increased
if (newMonth == 3 and newDay == 13 and newHour == 2 and minute > 0):
    newHour += 1
elif (newMonth == 3 and newDay == 13 and newHour > 2 and hour < 2):
    newHour += 1

# check daylight savings time to see if hour needs to be decreased
if (newMonth == 11 and newDay == 6 and newHour == 2 and minute > 0):
    newHour -= 1
elif (newMonth == 11 and newDay == 6 and newHour > 2 and hour < 2):
    newHour -= 1

# convert months under 10 to strings so they have the 0 in front of them
if (newMonth < 10):
    if (newMonth == 1):
        newMonth = '01'
    elif (newMonth == 2):
        newMonth = '02'
    elif (newMonth == 3):
        newMonth = '03'
    elif (newMonth == 4):
        newMonth = '04'
    elif (newMonth == 5):
        newMonth = '05'
    elif (newMonth == 6):
        newMonth = '06'
    elif (newMonth == 7):
        newMonth = '07'
    elif (newMonth == 8):
        newMonth = '08'
    elif (newMonth == 9):
        newMonth = '09'

# convert days under 10 to strings so they have the 0 in front of them
if (newDay < 10):
    if (newDay == 1):
        newDay = '01'
    elif (newDay == 2):
        newDay = '02'
    elif (newDay == 3):
        newDay = '03'
    elif (newDay == 4):
        newDay = '04'
    elif (newDay == 5):
        newDay = '05'
    elif (newDay == 6):
        newDay = '06'
    elif (newDay == 7):
        newDay = '07'
    elif (newDay == 8):
        newDay = '08'
    elif (newDay == 9):
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
    elif (newHour == 3):
        newHour = '03'
    elif (newHour == 4):
        newDay = '04'
    elif (newHour == 5):
        newDay = '05'
    elif (newHour == 6):
        newHour = '06'
    elif (newHour == 7):
        newHour = '07'
    elif (newHour == 8):
        newHour = '08'
    elif (newHour == 9):
        newHour = '09'

# calculate date and time to see if it is daylight savings time
# if so then change time during UTC before switching to new TZD

# print out new time for User
print(newMonth, newDay, newYear)
print(newHour , ":" , minute , ":" , newTZD)