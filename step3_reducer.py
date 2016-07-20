#!/usr/bin/env python
import sys
from datetime import datetime
from datetime import timedelta
import time
import decimal

current_site = None
combo = None
totalcount = 0

# input comes from STDIN
for line in sys.stdin:

	# remove leading and trailing whitespace
	line = line.strip()
	try:
		website, count = line.split('\t',1)
		
	except ValueError:
		continue

	if current_site == website:
		totalcount += int(count)

	else:
		if(current_site):
			print('%s\t%s' %(current_site, totalcount))
		current_site = website
		totalcount = int(count)

print('%s\t%s' %(current_site, totalcount))
