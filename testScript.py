# This script is to test the functionality of DateTime.py

import subprocess

print("DateTime.py Functionality Test!")
print("")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("")
print("Test Daylight savings time spring forward :")
print("python3 DateTime.py 03:12:2022:21:30:CDT UTC")
print("")
subprocess.call("python3 DateTime.py 03:12:2022:21:30:CDT UTC", shell=True)
print("")
print("Compare to :")
print("")
print("03 13 2022")
print("Saturday 03 : 30 : UTC")
print("")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("")
print("Test Daylight savings time fall back :")
print("python3 DateTime.py 11:05:2022:21:30:CDT UTC")
print("")
subprocess.call("python3 DateTime.py 11:05:2022:21:30:CDT UTC", shell=True)
print("")
print("Compare to :")
print("")
print("11 06 2022")
print("Saturday 01 : 30 : UTC")
print("")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("")
print("Test month and year change :")
print("python3 DateTime.py 12:31:2022:19:30:CDT UTC")
print("")
subprocess.call("python3 DateTime.py 12:31:2022:19:30:CDT UTC", shell=True)
print("")
print("Compare to :")
print("")
print("01 01 2023")
print("Saturday 00 : 30 : UTC")
print("")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
subprocess.call("python3 DateTime.py 11:28:2022:19:30:CDT UTC", shell=True)
print("")
print("Compare to :")
print("")
print("11 29 2022")
print("Monday 00 : 30 : UTC")
print("")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
subprocess.call("python3 DateTime.py 5:10:2020:19:30:CDT UTC", shell=True)
print("")
print("Compare to :")
print("")
print("05 11 2020")
print("Sunday 00 : 30 : UTC")
print("")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
