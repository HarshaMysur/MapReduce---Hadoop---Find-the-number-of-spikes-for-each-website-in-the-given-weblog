#!/usr/bin/env python
import sys
from datetime import datetime
from datetime import timedelta
import time
import decimal

FMT = '%H:%M:%S'
current_combo = None
combo = None
totalsec = 0

# input comes from STDIN
for line in sys.stdin:

	# remove leading and trailing whitespace
	line = line.strip()
	try:
		website, date, sec = line.split('\t',2)
		
	except ValueError:
		continue

	
	combo = website + ' ' + date
	if current_combo == combo:
		totalsec += int(sec)
		count += 1

	else:
		if current_combo:
			oldwebsite, olddate = current_combo.split()
			avgsec = float(totalsec)/count
			print('%s\t%s\t%s' %(oldwebsite, olddate, avgsec))
			
		totalsec = int(sec)
		current_combo = combo
		count = 1

oldwebsite, olddate = combo.split()
avgsec = round(totalsec/count)
print('%s\t%s\t%s' %(oldwebsite, olddate, avgsec))
