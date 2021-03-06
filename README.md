# Final project

CS5103_VTF657_BrandonHuschle

## Date Time Transformation

### Second Requirements
Transform the given date and time zone to any different given date and time zone  
add functionality which allows adding daylight-saving starting date time and daylight-saving ending date time  
Assume that all time zones share the same starting / ending date time

#### How to use
> python3 DateTime.py MM:DD:YYYY:hh:mm:TZD newTZD

MM     = month  
DD     = day  
YYYY   = year  
hh     = hour  
mm     = minute  
TZD    = Time Zone   
newTZD = new Time Zone  
Must be used with Military Time  
Only used with American based Time zones  

#### List of Time zones
HST - Hawaii Standard Time  
HDT - Hawaii-Aleutian Daylight Time  
AKDT - Alaska Daylight Time  
PDT - Pacific Daylight Time  
MST - Mountain Standard Time  
MDT - Mountain Daylight Time  
CDT - Central Daylight Time  
EDT - Eastern Daylight Time  

#### How to run test script
> python3 testScript.py

This will run multiple tests on the program  
- Spring Forward _ March 12th after 2am
- Fall back _ November 6th after 2am
- Month and year change

#### BONUS
- try running the program without any options
- try running the program with a TZD that is not listed
- try running the program with the -h option
- try running the program with the -tzd option