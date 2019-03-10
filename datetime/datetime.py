#!/usr/bin/env python
import datetime
execfile("/kwh/config/load_config.py")

dtm = datetime.datetime.today()
dstr=str(dtm)

with open('/kwh/datetime/datetime', 'w') as df:
# Depricated format
#	df.write(dstr[5:7]+'/'+dstr[8:10]+'/'+dstr[:4]+','+dstr[11:19])
	df.write(dstr)
