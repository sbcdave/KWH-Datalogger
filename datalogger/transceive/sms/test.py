#!/usr/bin/env python

import re

analogIn = re.compile(\
r"\w*\s*(\d{4})#GIP:(\d*)()#\s*\w*")

match = analogIn.search("1111#GIP:10001#")


if match.group(3):
	print "yep"
