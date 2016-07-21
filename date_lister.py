# Generates a printout of date stamps for the next year. Whoof!
# For more date formatting check out the [documentation](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior)

import sys, os, re
import time, datetime

# .... constants
doWeekendColor = True # .... change this if u like!
weekendColor = "#ffdd99" # .... change this if u like!
weekend = set([5, 6])

# .... let's go!
daty = datetime.date.today() # - datetime.timedelta(days=30)

for i in range(365):
	dateStr = "{:%a/%b %d/%Y}".format(daty)
	if daty.weekday() == 0:
		print ("----------------------------------------------------------------------\n")
	if doWeekendColor and daty.weekday() in weekend:
		dateStr = "<font color='{1}'>{0}</font>".format(dateStr, weekendColor)
	print (dateStr)
	print ("---\n\n\n")
	daty += datetime.timedelta(days=1)
