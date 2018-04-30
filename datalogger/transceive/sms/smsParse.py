#!/usr/bin/env python

import re
import subprocess
import time

p = subprocess.Popen("/KWH/datalogger/transceive/sms/smsRead.sh")
# Wait for smsRead to complete
p.communicate()

getMsgData = re.compile("\+CMGL:.*")

msgNum = 1

# Used to skip the first non relevant lines
inMsg = False

# Used to skip close on first temp file opening
tempOpen = False

time.sleep(1)

log = open("/KWH/datalogger/transceive/sms/read.log", 'r+')
while True:
    line = log.readline()
    if not line: break
    if getMsgData.search(line) or inMsg:
        inMsg = True
        if getMsgData.search(line):
            if tempOpen: temp.close()
            temp = open("/KWH/datalogger/transceive/sms/msg/msg"+str(msgNum), 'w+')
            tempOpen = True
            msgNum = msgNum + 1
        temp.write(line)

log.close()
temp.close()

p = subprocess.Popen("/KWH/datalogger/transceive/sms/smsProcess.py")
p.communicate()

p = subprocess.Popen("/KWH/datalogger/transceive/sms/cleanMsg.sh")
p.communicate()
