#!/usr/bin/env python

import re
import subprocess
import time

# Load environment variables
execfile("/kwh/config/load_config.py")
DEBUG = int(DEBUG)

if DEBUG: print("Running smsRead.sh")
p = subprocess.Popen("/kwh/transceive/sms/smsRead.sh")
# Wait for smsRead to complete
p.communicate()

if DEBUG: print("Running smsDelAll.sh")
p = subprocess.Popen("/kwh/transceive/sms/smsDelAll.sh")
p.communicate()

getMsgData = re.compile("\+CMGL:.*")

msgNum = 1

# THIS CODE HAS A BUG THAT IT WILL THROW AN EXCEPTION IF THERE IS NO
# MESSAGE TO READ. IT STILL WORKS, BUT IT WOULD BE NICE TO FIX THAT
# BUG

# Used to skip the first non relevant lines
inMsg = False

# Used to skip close on first temp file opening
tempOpen = False

time.sleep(1)

if DEBUG: print("Building files in msg/")
log = open("/kwh/transceive/sms/read.log", 'r+')
while True:
    line = log.readline()
    if not line: break
    if getMsgData.search(line) or inMsg:
        inMsg = True
        if getMsgData.search(line):
            if tempOpen: temp.close()
            temp = open("/kwh/transceive/sms/msg/msg"+str(msgNum), 'w+')
            tempOpen = True
            msgNum = msgNum + 1
        temp.write(line)

log.close()
temp.close()

if DEBUG: print("Running smsProcess.py")
p = subprocess.Popen("/kwh/transceive/sms/smsProcess.py")
p.communicate()

if DEBUG: print("Running cleanMsg.sh")
p = subprocess.Popen("/kwh/transceive/sms/cleanMsg.sh")
p.communicate()
