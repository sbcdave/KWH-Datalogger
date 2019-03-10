#!/usr/bin/env python

import re
import subprocess
import os
import mmap

# Load environment variables
execfile("/KWH/config/pyvars.py")
DEBUG = int(DEBUG)
smsPath = "/KWH/transceive/sms"

# Setup regex and paths to command scripts
sendPath = smsPath+"/smsSend.sh"
commandList = []
################################################################################
admpwPath = smsPath+"/commands/ADMPW.sh"
admpw = re.compile(r"(.*?)#ADM:(.*?)()#")
commandList.append(admpw)
################################################################################
adxxPath = smsPath+"/commands/ADxx.sh" 
adxx = re.compile(\
r"(.*?)#AD(\d\d):([0-1])(,\d.\d{3},\d.\d{3},\d.\d{3},\d.\d{3},\d.\d{3},[0,1]{4},[0-3]{6})*?#")
commandList.append(adxx)
################################################################################
apnPath = smsPath+"/commands/APN.sh" 
apn = re.compile(r"(.*?)#APN:(.*?)#") 
commandList.append(apn)
################################################################################
debugPath = smsPath+"/commands/DEBUG.sh" 
debug = re.compile(r"(.*?)#DBG:([0-1])#")
commandList.append(debug)
################################################################################
domainPath = smsPath+"/commands/DOMAIN.sh" 
domain = re.compile(r"(.*?)#DOM:(.*?)#") 
commandList.append(domain)
################################################################################
inqConfPath = smsPath+"/commands/inqConf.sh" 
inqConf = re.compile(r"(.*?)#CONF#") 
commandList.append(inqConf)
################################################################################
inqValPath = "/KWH/transceive/tcp"
inqVal = re.compile(r"(.*?)#VAL#") 
commandList.append(inqVal)
################################################################################
portPath = smsPath+"/commands/PORT.sh" 
port = re.compile(r"(.*?)#PORT:(\d{1,5})#") 
commandList.append(port)
################################################################################
puxxPath = smsPath+"/commands/PUxx.sh" 
puxx = re.compile(r"(.*?)#PU(\d\d):([0-1])(,[0-1]{4},[0-3]{6})*?#") 
commandList.append(puxx)
################################################################################
puxxValPath = smsPath+"/commands/PUxxVal.sh" 
puxxVal = re.compile(r"(.*?)#PU(\d\d)VAL:(\d*)#") 
commandList.append(puxxVal)
################################################################################
resetPath = smsPath+"/commands/RESET.sh" 
reset = re.compile(r"(.*?)#RESET#") 
commandList.append(reset)
################################################################################
staPath = smsPath+"/commands/STA.sh" 
sta = re.compile(r"(.*?)#STA:(.*?)#") 
commandList.append(sta)
################################################################################
tx_intrvlPath = smsPath+"/commands/TX_INTRVL.sh"
tx_intrvl = re.compile(r"(.*?)#TX:(\d*?)#")
commandList.append(tx_intrvl)
################################################################################
invalid = re.compile(r"(.*?)#")
commandList.append(invalid)
################################################################################


##### MAIN #####
# smsParse.py reads all sms into individual files in smsPath/msg directory
# This puts them all into an array in message numerical order
messages = os.listdir(smsPath+"/msg")
messages.sort()
# Regex to get message #, phone #, and msg data from each message
messageData = re.compile(r"\+CMGL: \d*,.*?,(.*?),.*?,.*?\n(.*)")
# This array will be populated with the msg(s) that each have the 3 regex groups
msgList = []

if DEBUG: print messages
for msg in messages:
    # Exclude the .gitMarker file that is only there so GitHub will retain the directory
    if str(msg) <> ".gitMarker":
        if DEBUG: print smsPath+"/msg/"+str(msg)
        f = open(smsPath+"/msg/"+str(msg), 'r+')
        msgData = mmap.mmap(f.fileno(), 0)
        parts = messageData.search(msgData)
        msgList.append([parts.group(1).replace('"', ''), parts.group(2)])
        if DEBUG: print msgList
        f.close()

# NOTE: msg[0] = phone number, msg[1] = the message
for msg in msgList:
    found = False
    for command in commandList:
        match = command.search(msg[1]) 
        if match and not found:
	    found = True
            # Execute the corresponding command file and pass it the msg data
            if command == reset:
	        if match.group(1) == ADMPW:
                    if DEBUG: print("Password match")
                    p = subprocess.Popen([resetPath, msg[0]])
                    p.communicate()
            elif command == admpw:
	        if match.group(1) == ADMPW:
                    if DEBUG: print("Password match")
                    p = subprocess.Popen([admpwPath, msg[0], match.group(2)])
                    p.communicate()
            elif command == sta:
	        if match.group(1) == ADMPW:
                    if DEBUG: print("Password match")
                    p = subprocess.Popen([staPath, msg[0], match.group(2)])
                    p.communicate()
            elif command == debug:
	        if match.group(1) == ADMPW:
                    if DEBUG: print("Password match")
                    p = subprocess.Popen([debugPath, msg[0], match.group(2)])
                    p.communicate()
            elif command == domain:
	        if match.group(1) == ADMPW:
                    if DEBUG: print("Password match")
                    p = subprocess.Popen([domainPath, msg[0], match.group(2)])
                    p.communicate()
            elif command == port:
	        if match.group(1) == ADMPW:
                    if DEBUG: print("Password match")
                    p = subprocess.Popen([portPath, msg[0], match.group(2)])
                    p.communicate()
            elif command == apn:
	        if match.group(1) == ADMPW:
                    if DEBUG: print("Password match")
                    p = subprocess.Popen([apnPath, msg[0], match.group(2)])
                    p.communicate()
            elif command == puxx:
	        if match.group(1) == ADMPW:
                    if DEBUG: print("Password match")
                    p = subprocess.Popen([puxxPath, msg[0], match.group(2), match.group(3)])
                    p.communicate()
            elif command == puxxVal:
	        if match.group(1) == ADMPW:
                    if DEBUG: print("Password match")
                    p = subprocess.Popen([puxxValPath, msg[0], match.group(2), match.group(3)])
                    p.communicate()
            elif command == adxx:
	        if match.group(1) == ADMPW:
                    if DEBUG: print("Password match")
                    p = subprocess.Popen([adxxPath, msg[0], match.group(2), match.group(3)])
                    p.communicate()
            elif command == tx_intrvl:
	        if match.group(1) == ADMPW:
                    if DEBUG: print("Password match")
                    p = subprocess.Popen([tx_intrvlPath, msg[0], match.group(2)])
                    p.communicate()
            elif command == inqConf:
	        if match.group(1) == ADMPW:
                    if DEBUG: print("Password match")
                    p = subprocess.Popen([inqConfPath, msg[0]])
                    p.communicate()
            elif command == inqVal:
	        if match.group(1) == ADMPW:
                    if DEBUG: print("Password match")
                    p = subprocess.Popen([inqValPath+"/tstring.py"])
                    p.communicate()
                    with open(inqValPath+"/tstring", "r") as val:
			data=val.read().replace(';', ' ')
                    p = subprocess.Popen([sendPath, msg[0], data])
                    p.communicate()
            elif command == invalid:
	        if match.group(1) == ADMPW:
                    if DEBUG: print("Password match")
                    p = subprocess.Popen([sendPath, msg[0], "Command not valid"])
		    p.communicate()
