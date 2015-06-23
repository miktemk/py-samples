# Generates a printout of date stamps for the next year. Whoof!
# For more date formatting check out the [documentation](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior)

import sys, os, re
import time, datetime

daty = datetime.date.today()

for i in range(365):
	dateStr = "{:%a/%b %d/%Y}".format(daty)
	print (dateStr)
	print ("---\n\n\n")
	daty += datetime.timedelta(days=1)
