#!/usr/bin/env python

import sys

path = "/KWH/datalogger/pulse/PU0"+sys.argv[1]

with open(path, 'w+') as update:
	update.write(sys.argv[2])
