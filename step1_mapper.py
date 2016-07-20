#!/usr/bin/env python

import sys
from datetime import datetime
from datetime import timedelta
import re

FMT = '%H:%M:%S'

for line in sys.stdin:
	line = line.strip()
	try:
		website, stdt, eddt = line.split('\t', 2)
	except ValueError:
		continue
	
	time1 = (datetime.strptime(stdt[11:], FMT)).time()
	time2 = (datetime.strptime(eddt[11:], FMT)).time()
	if(time1 > time2):
		sec = (datetime.strptime('23:59:59', FMT) - datetime.strptime(stdt[11:], FMT)).seconds
		sec += (datetime.strptime(eddt[11:], FMT) - datetime.strptime('00:00:00', FMT)).seconds
		sec += 1
	else:
		sec = (datetime.strptime(eddt[11:], FMT) - datetime.strptime(stdt[11:], FMT)).seconds

	print('%s\t%s\t%s' % (website, stdt[:10], sec))