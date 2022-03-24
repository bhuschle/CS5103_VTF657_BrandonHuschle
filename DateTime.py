# Brandon Huschle _ VTF657
# CS5103 Final Project
# transform datetime string to different time zone
# add information needed for calculating daylight savings time
# MM:DD:YYYY:hh:mm:TZD newTZD  <- month:day:year:Military time : TZD = Time Zone Designator
# EX : 12:21:2022:15:30:UTC

import sys


# Check to see if user input any information
if len(sys.argv) == 1:
    print("Please add the correct information when running the program")
    print("Run \"python3 DateTime.py -h\" if you need help")
    sys.exit()

# Grab user input
userInput = sys.argv[1]

if userInput == '-h':
    print("Please run the code with the following format :")
    print()
    print("\"python3 DateTime.py MM:DD:YYY:hh:mm:TZD newTZD\"")
    print()
    print("MM   = Month")
    print("DD   = Day")
    print("YYYY = Year")
    print("hh   = Hour")
    print("mm   = Minute")
    print("TZD  = Time Zone Designator")
    print()
    print("Available Time Zone Designators to choose from :")
    print()
    print("HST  - Hawaii Standard Time")
    print("HDT  - Hawaii-Aleutian Daylight Time")
    print("AKDT - Alaska Daylight Time")
    print("PDT  - Pacific Daylight Time")
    print("MST  - Mountain Standard Time")
    print("MDT  - Mountain Daylight Time")
    print("CDT  - Central Daylight Time")
    print("EDT  - Eastern Daylight Time")
    sys.exit()

if userInput == '-tzd':
    print("Available Time Zone Designators to choose from :")
    print()
    print("HST  - Hawaii Standard Time")
    print("HDT  - Hawaii-Aleutian Daylight Time")
    print("AKDT - Alaska Daylight Time")
    print("PDT  - Pacific Daylight Time")
    print("MST  - Mountain Standard Time")
    print("MDT  - Mountain Daylight Time")
    print("CDT  - Central Daylight Time")
    print("EDT  - Eastern Daylight Time")
    sys.exit()

userInput = userInput.split(":")

month = int(userInput[0])
day = int(userInput[1])
year = int(userInput[2])
hour = int(userInput[3])
minute = int(userInput[4])
tzd = userInput[5]

# Test that information split properly
# print(month, day, year, hour, minute, tzd)

# initialize new hour variable to make changes
newHour = hour

# Convert to UTC
if (tzd == 'HST'):
    newHour += 10
elif (tzd == 'HDT'):
    newHour += 9
elif (tzd == 'AKDT'):
    newHour += 8
elif (tzd == 'PDT'):
    newHour += 7
elif (tzd == 'MST'):
    newHour += 7
elif (tzd == 'CDT'):
    newHour += 5
elif (tzd == 'EDT'):
    newHour += 4
else:
    print("You have not entered a valid TZD")
    print("Run program with this format to see TZD options :")
    print("\"python3 DateTime.py -tzd\"")
    sys.exit()

# Grab wanted new TZD
newTZD = sys.argv[2]

# Convert UTC to new tzd
if (newTZD == 'HST'):
    newHour -= 10
elif (newTZD == 'HDT'):
    newHour -= 9
elif (newTZD == 'AKDT'):
    newHour -= 8
elif (newTZD == 'PDT'):
    newHour -= 7
elif (newTZD == 'MST'):
    newHour -= 7
elif (newTZD == 'CDT'):
    newHour -= 5
elif (newTZD == 'EDT'):
    newHour -= 4
elif (newTZD == 'UTC'):
    newHour = newHour
else:
    print("You have not entered a valid TZD")
    sys.exit()

# initialize new variables for month, day, year
newMonth = month
newDay = day
newYear = year

# check hour and minute to see if date will have changed
if (newHour == 24):
    newHour = '00'
    newDay += 1
elif (newHour > 24):
    newHour -= 24
    newDay += 1

# check that the month has not changed
thirtyOne = [1, 3, 5, 7, 8, 10, 12]
if (newMonth in thirtyOne and newDay > 31):
    if (newMonth == 12):
        newDay -= 31
        newMonth = 1
        newYear += 1
    else:
        newDay -= 31
        newMonth += 1
elif (newMonth == 2 and newDay > 28):
    newDay -= 28
    newMonth += 1
else:
    if (newDay > 30):
        newDay -= 30
        newMonth += 1

# check daylight savings time to see if hour needs to be increased
if (newMonth == 3 and newDay == 13 and newHour == 2 and minute > 0):
    newHour += 1
elif (newMonth == 3 and newDay == 13 and newHour > 2 and hour < 2):
    newHour += 1
elif (newMonth == 3 and newDay == 13 and newHour > 2 and day == 12):
    newHour += 1

# check daylight savings time to see if hour needs to be decreased
if (newMonth == 11 and newDay == 6 and newHour == 2 and minute > 0):
    newHour -= 1
elif (newMonth == 11 and newDay == 6 and newHour > 2 and hour < 2):
    newHour -= 1
elif (newMonth == 11 and newDay == 6 and newHour > 2 and day == 10):
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

# convert hours under 10 to strings so they have the 0 in front of them
if (newHour != '00' and newHour < 10):
    if (newHour == 1):
        newHour = '01'
    elif (newHour == 2):
        newHour = '02'
    elif (newHour == 3):
        newHour = '03'
    elif (newHour == 4):
        newHour = '04'
    elif (newHour == 5):
        newHour = '05'
    elif (newHour == 6):
        newHour = '06'
    elif (newHour == 7):
        newHour = '07'
    elif (newHour == 8):
        newHour = '08'
    elif (newHour == 9):
        newHour = '09'

# print out new time for User
print(newMonth, newDay, newYear)
print(newHour , ":" , minute , ":" , newTZD)
