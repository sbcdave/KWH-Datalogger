#!/usr/bin/env python
import re

analogIn = re.compile(\
r"\w*\s*(\d{4})#ADN(\d*):([0-2]),(\d.\d{3}),(\d.\d{3}),(\d.\d{3}),(\d.\d{3}),(\d.\d{3}),([0,1]{4}),([0-3]{6})#\s*\w*")
match = analogIn.search("1111#ADN04:0,0.000,0.000,0.000,0.000,0.000,0000,000000#")
print match.group(1)
print match.group(2)
print match.group(3)
