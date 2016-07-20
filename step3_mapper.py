#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
	#line = line.strip()
	website, count = line.split('\t', 1)
	print('%s\t%s' % (website, count))