#!/usr/bin/env python

import re
import subprocess
import os
import mmap

# Load environment variables
execfile("/KWH/datalogger/config/pyvars.py")
DEBUG = int(DEBUG)

#File paths for processing
delPath ="/KWH/datalogger/transceive/sms/smsDel.sh"
sendPath = "/KWH/datalogger/transceive/sms/smsSend.sh"

#Bash command paths for processing
resetPath = "/KWH/datalogger/transceive/sms/commands/reset.sh"
inqGSMPath = "/KWH/datalogger/transceive/sms/commands/inquiryGSM.sh"
setDigInPath = "/KWH/datalogger/transceive/sms/commands/setDigitalIn.sh"
setPulsePath = "/KWH/datalogger/transceive/sms/commands/setPulsePath.py"
portPath = "/KWH/datalogger/transceive/sms/commands/port.sh"
staPath = "/KWH/datalogger/transceive/sms/commands/sta.sh"
setInqPassPath = "/KWH/datalogger/transceive/sms/commands/inq.sh"
domainPath = "/KWH/datalogger/transceive/sms/commands/domain.sh"
setApnPath = "/KWH/datalogger/transceive/sms/commands/apn.sh"
analogInPath = "/KWH/datalogger/transceive/sms/commands/analogIn.sh"
tempAnalogInPath = "/KWH/datalogger/transceive/sms/commands/tempAnalogIn.sh"
inqE2Path = "/KWH/datalogger/transceive/sms/commands/inqE2.sh"
inqEEPath = "/KWH/datalogger/transceive/sms/commands/inqEE.sh" 

#Regex to grab import groups from message data
messageData = re.compile(r"\+CMGL: (\d*),.*?,(.*?),.*?,.*?\n(.*)")

#Regex to decipher incoming commands
reset = re.compile(\
r"(.*?)#RESET#")
stationId = re.compile(\
r"(.*?)#BST:(.*?)()#")
setInquiryPass = re.compile(\
r"(.*?)#BPS:(\d{4}),(\d{4})#")
setServerDNS = re.compile(\
r"(.*?)#GDN:([A-z\.]*)()\!#")
setServerPort = re.compile(\
r"(.*?)#GIP:(\d{1,5})()#")
setupAPN = re.compile(\
r"(.*?)#GAN:(\w*)()\!#")
inquiryGSM = re.compile(\
r"(.*?)#E1#")
setDigitalInputParams = re.compile(\
r"(.*?)#DIN([1-8]):([0-4]),([0-1]{4}),([0-3]{6})#")
setPulseCounter = re.compile(\
r"(.*?)#DIP([1-8]):(\d*)#")
analogIn = re.compile(\
r"(.*?)#ADN(\d*):([0-2]),(\d.\d{3}),(\d.\d{3}),(\d.\d{3}),(\d.\d{3}),(\d.\d{3}),([0,1]{4}),([0-3]{6})#")
tempAnalogIn = re.compile(\
r"(.*?)#ADN(1[1,2]):([0-2]),(\d.\d{3}),(\d.\d{3}),([0-1]{4}),([0-3]{6})#")
inquiryE2 = re.compile(\
r"(.*?)#E2#")
inquiryEE = re.compile(\
r"(.*?)#EE#")
invalid = re.compile(\
r"(.*?)#")
catchAll = re.compile(\
r".*")

commandList = [reset, stationId, setInquiryPass, setServerDNS, setServerPort, setupAPN, inquiryGSM,\
 setDigitalInputParams, setPulseCounter, analogIn, tempAnalogIn, inquiryE2, inquiryEE, invalid, catchAll] 

# msg[0] = message number, msg[1] = phone number, msg[2] = the message
def process(options, commandFile, msg):
    if DEBUG: print("Set "+options[0])
    #If password is good call the command file
    if match.group(1) == ADMPW:
        if DEBUG: print("Password match")
	if match.group(3) <> '':
                if DEBUG: print("Setting "+options[0]+" "+match.group(2)+" to: "+match.group(3))
	        p = subprocess.Popen([commandFile, str(match.group(2)), str(match.group(3))])
	else:
                if DEBUG: print("Setting "+options[0]+" to: "+match.group(2))
        	p = subprocess.Popen([commandFile, str(match.group(2))])
        # wait until complete to start delete process
        p.communicate()
        if p.returncode == 0:
            if DEBUG: print(options[0]+" set success")
            if DEBUG: print("Deleting sms #"+msg[0])
            p = subprocess.Popen([delPath, msg[0]])
            p.communicate()
            if p.returncode == 0:
                if DEBUG: print("Delete success")
            else:
                if DEBUG: print("Delete failed")
            if DEBUG: print("Executing: "+sendPath+" "+msg[1]+" "+options[0]+" set to: "+match.group(2))
	    if match.group(3) <> '':
                p = subprocess.Popen([sendPath, msg[1], str(options[0])+" "+str(match.group(2))+" set to: "+str(match.group(3))])
	    else:
                p = subprocess.Popen([sendPath, msg[1], str(options[0])+" set to: "+str(match.group(2))])
            p.communicate()
    else:
        if DEBUG: print("Wrong password")
        if DEBUG: print("Deleting sms #"+msg[0])
        p = subprocess.Popen([delPath, msg[0]])
        p.communicate()
        if p.returncode == 0:
            if DEBUG: print("Delete success")
        else:
            if DEBUG: print("Delete failed")

#MAIN
msgList = []
messages = os.listdir("/KWH/datalogger/transceive/sms/msg")
messages.sort()
if DEBUG: print messages
for msg in messages:
    if DEBUG: print "/KWH/datalogger/transceive/sms/msg/"+str(msg)
    f = open("/KWH/datalogger/transceive/sms/msg/"+str(msg), 'r+')
    msgData = mmap.mmap(f.fileno(), 0)
    parts = messageData.search(msgData)
    msgList.append([parts.group(1), parts.group(2).replace('"', ''), parts.group(3)])
    if DEBUG: print msgList
    f.close()

for msg in msgList:
    found = False
    for command in commandList:
        match = command.search(msg[2]) 
        if match and not found:
	    found = True
        #Execute the appropriate processing file
            if command == reset:
                if DEBUG: print("reset")
            elif command == stationId:
		process(["Station ID"], staPath, msg)
	    elif command == setInquiryPass:
		process(["Inquiry Password"], inqPath, msg)
            elif command == setServerDNS:
		process(["Server Domain"], domainPath, msg)
            elif command == setServerPort:
		process(["Server Port"], portPath, msg)                
            elif command == setupAPN:
		process(["APN"], apnPath, msg)
            elif command == inquiryGSM:
                if DEBUG: print(["inquiry GSM"])
            elif command == setDigitalInputParams:
                if DEBUG: print(["set digital input params"])
            elif command == setPulseCounter:
                process(["Pulse Channel"], setPulsePath, msg)
            elif command == analogIn:
		process(["Analog Channel"], analogInPath, msg)
                if DEBUG: print(["analog in"])
            elif command == tempAnalogIn:
                if DEBUG: print(["temperature analog in"])
            elif command == inquiryE2:
                if DEBUG: print(["inquiry E2"])
            elif command == inquiryEE:
                if DEBUG: print(["inquiry EE"])
            elif command == invalid:
	        if match.group(1) == ADMPW:
                    p = subprocess.Popen([sendPath, msg[1], "Command not valid"])
		    p.communicate()	    
                    p = subprocess.Popen([delPath, msg[0]])
		    p.communicate()
                    if DEBUG: print("Deleting invalid message with correct password")
	    elif command == catchAll:
                p = subprocess.Popen([delPath, msg[0]])
                p.communicate()
                if DEBUG: print("Deleting invalid message without correct password")
