Brandon Huschle - VTF657

#CS5103 - Final Project

## Requirements

Date Time Transformation

- Transform the given datetime string to different formats
- Must be able to transform to any different time zone
- Add daylight-saving mode
  - Assume that all time zones share the same starting / ending date time
- Have the program recognize the day of the week and display it with the new day/time

## User Stories

- As Max, I want to be able to check the time of my friend that lives in Hawaii while I am in Texas
  - python3 DateTime.py 01:12:2022:15:40:CDT HDT
- As Jordyn, I want to be able to see what time my 5 hour flight lands in CT while I am in California
  - python3 DateTime.py 12:25:2023:18:55:MDT EST
- As Sascha, I want to be able to see what time I will reach illinois on my drive from Florida
  - python3 DateTime.py 03:12:2019:12:15:EST CDT
- As a manager, I want to know what time my employee that lives in Colorado will sign on for a meeting
  - python3 DateTime.py 09:05:2020:09:00:EST CDT
- As a tech expert, I want to know what time the update from cupertino will launch while i Live in Maine
  - python3 DateTime.py 07:21:2021:08:35:EST MST
- As a Virtual Employee, I need to know what time work starts tomorrow in New Jersey while I live in New Mexico
  - python3 DateTime.py 05:19:2022:08:30:CDT EST
- As a 9-5 monday-friday worker I want to know if I go from Maine to California if I will need to work that day
  - python3 DateTime.py 07:21:2021:08:35:EST MST

## Design change

I did not have very much of a design change when it came to implementing this project. The only changes I made were to implement the requirements that were put forth. I was able to do these fairly simple with the simplicity of python and being able to add to projects with the language. I was also lucky enough that python had a built in tool that allowed me to show the day of the week by just parsing the month date and year. This made the final requirement very easy to implement.

## Static bug detection

I used pylint to do some static bug detection.

**\*\***\***\*\*** Module DateTime
DateTime.py:74:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
DateTime.py:76:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:78:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:80:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:82:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:84:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:86:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:98:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
DateTime.py:100:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:102:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:104:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:106:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:108:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:110:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:112:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:124:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
DateTime.py:127:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:134:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
DateTime.py:145:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
DateTime.py:168:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
DateTime.py:169:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
DateTime.py:171:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:173:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:175:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:177:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:179:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:181:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:183:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:185:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:189:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
DateTime.py:190:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
DateTime.py:192:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:194:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:196:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:198:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:200:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:202:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:204:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:206:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:211:0: C0325: Unnecessary parens after 'if' keyword (superfluous-parens)
DateTime.py:213:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:215:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:217:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:219:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:221:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:223:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:225:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:227:0: C0325: Unnecessary parens after 'elif' keyword (superfluous-parens)
DateTime.py:1:0: C0103: Module name "DateTime" doesn't conform to snake_case naming style (invalid-name)
DateTime.py:1:0: C0114: Missing module docstring (missing-module-docstring)
DateTime.py:113:4: W0127: Assigning the same variable 'newHour' to itself (self-assigning-variable)
DateTime.py:125:4: C0103: Constant name "newHour" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:136:8: C0103: Constant name "newMonth" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:152:6: R1716: Simplify chained comparison between the operands (chained-comparison)
DateTime.py:160:6: R1716: Simplify chained comparison between the operands (chained-comparison)
DateTime.py:165:10: E1101: Module 'datetime' has no 'date' member (no-member)
DateTime.py:170:8: C0103: Constant name "newMonth" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:172:8: C0103: Constant name "newMonth" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:174:8: C0103: Constant name "newMonth" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:176:8: C0103: Constant name "newMonth" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:178:8: C0103: Constant name "newMonth" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:180:8: C0103: Constant name "newMonth" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:182:8: C0103: Constant name "newMonth" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:184:8: C0103: Constant name "newMonth" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:186:8: C0103: Constant name "newMonth" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:191:8: C0103: Constant name "newDay" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:193:8: C0103: Constant name "newDay" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:195:8: C0103: Constant name "newDay" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:197:8: C0103: Constant name "newDay" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:199:8: C0103: Constant name "newDay" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:201:8: C0103: Constant name "newDay" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:203:8: C0103: Constant name "newDay" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:205:8: C0103: Constant name "newDay" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:207:8: C0103: Constant name "newDay" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:212:8: C0103: Constant name "newHour" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:214:8: C0103: Constant name "newHour" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:216:8: C0103: Constant name "newHour" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:218:8: C0103: Constant name "newHour" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:220:8: C0103: Constant name "newHour" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:222:8: C0103: Constant name "newHour" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:224:8: C0103: Constant name "newHour" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:226:8: C0103: Constant name "newHour" doesn't conform to UPPER_CASE naming style (invalid-name)
DateTime.py:228:8: C0103: Constant name "newHour" doesn't conform to UPPER_CASE naming style (invalid-name)

---

Your code has been rated at 5.22/10

This was the output I received. This was very surprising to me because I believed that I had coded to most normal standards. This made me rethink and relook at how I have been programming in the past and realize that I need to look much more into coding standards for python. Especially because python is a language I enjoy and would like to spend more time using. Overall even though the rate was lower then expected there was no high level bugs or problems with my code other then what is the norm of coding standards for python so I feel quite good about the results that I received.
