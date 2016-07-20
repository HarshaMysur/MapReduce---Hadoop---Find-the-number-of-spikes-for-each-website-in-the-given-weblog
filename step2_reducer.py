#!/usr/bin/env python
import sys
from datetime import datetime
from datetime import timedelta
import time

FMT = '%Y-%m-%d'
current_site = None

# input comes from STDIN
for line in sys.stdin:

	# remove leading and trailing whitespace
	line = line.strip()
	try:
		website, date, curr_sec = line.split('\t',2)
		
	except ValueError:
		continue

	curr_date = datetime.strptime(date, FMT)

	if current_site == website:
		if (curr_date == date1 + timedelta(days=1)) and (float(curr_sec) >= 2 * float(sec1)):
			initdate = curr_date
			initsec = curr_sec
		
		elif (curr_date == date1 + timedelta(days=2)) and (float(curr_sec) >= 2 * 2 * float(sec1)):
			if (curr_date == initdate + timedelta(days=1)) and (float(curr_sec) >= 2 * float(initsec)):
				date1 = initdate
				sec1 = initsec 
				initdate = curr_date
				initsec = curr_sec
				print('%s\t%s' %(website, 1))

			else:
				date1 = curr_date
				sec1 = curr_sec
		else:
			date1 = curr_date
			sec1 = curr_sec

	else:
		current_site = website
		date1 = curr_date
		sec1 = curr_sec
