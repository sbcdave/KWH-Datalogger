#!/usr/bin/env python

#Process the data
import subprocess
import string
import sys

processFile = "/KWH/datalogger/conf/setConf.sh"

#example update
keyword = PORT
val = 11001


#Process the update
#should loop through all the things that are left to be processed
subprocess.Popen([processFile, keyword, str(val)])
