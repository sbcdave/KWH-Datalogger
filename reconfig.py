#!/usr/bin/env python

# Reconfigure script will run through the
# list of variables and present a defualt value for them
# the user may opt to change the values

import re
import subprocess
import string

analogList = ["AD01", "AD02", "AD03", "AD04", "AD05", "AD06", "AD07", "AD08", "AD09", "AD10", "AD11", "AD12", "AD13", "AD14", "AD15", "AD16", "AD17", "AD18"]

pulseList = ["PU01", "PU02", "PU03", "PU04", "PU05", "PU06", "PU07", "PU08"]

passList = ["Administration Password", "Inquiry Password"]


#file paths for updating
domPath = "/KWH/datalogger/transceive/sms/commands/domain.sh"
ApassPath = "/KWH/datalogger/transceive/sms/commands/aPass.sh"
IpassPath = "/KWH/datalogger/transceive/sms/commands/iPass.sh"
portPath = "/KWH/datalogger/transceive/sms/commands/port.sh"
apnPath = "/KWH/datalogger/transceive/sms/commands/apn.sh"
txPath = "/KWH/datalogger/transceive/sms/commands/tx.sh"
debugPath = "/KWH/datalogger/transceive/sms/commands/debug.sh"
staPath = "/KWH/datalogger/transceive/sms/commands/sta.sh"
AD01Path = "/KWH/datalogger/transceive/sms/commands/AD01.sh"
AD02Path = "/KWH/datalogger/transceive/sms/commands/AD02.sh"
AD03Path = "/KWH/datalogger/transceive/sms/commands/AD03.sh"
AD04Path = "/KWH/datalogger/transceive/sms/commands/AD04.sh"
AD05Path = "/KWH/datalogger/transceive/sms/commands/AD05.sh"
AD06Path = "/KWH/datalogger/transceive/sms/commands/AD06.sh"
AD07Path = "/KWH/datalogger/transceive/sms/commands/AD07.sh"
AD08Path = "/KWH/datalogger/transceive/sms/commands/AD08.sh"
AD09Path = "/KWH/datalogger/transceive/sms/commands/AD09.sh"
AD10Path = "/KWH/datalogger/transceive/sms/commands/AD10.sh"
AD11Path = "/KWH/datalogger/transceive/sms/commands/AD11.sh"
AD12Path = "/KWH/datalogger/transceive/sms/commands/AD12.sh"
AD13Path = "/KWH/datalogger/transceive/sms/commands/AD13.sh"
AD14Path = "/KWH/datalogger/transceive/sms/commands/AD14.sh"
AD15Path = "/KWH/datalogger/transceive/sms/commands/AD15.sh"
AD16Path = "/KWH/datalogger/transceive/sms/commands/AD16.sh"
AD17Path = "/KWH/datalogger/transceive/sms/commands/AD17.sh"
AD18Path = "/KWH/datalogger/transceive/sms/commands/AD18.sh"

PU01Path = "/KWH/datalogger/transceive/sms/commands/PU01.sh"
PU02Path = "/KWH/datalogger/transceive/sms/commands/PU02.sh"
PU03Path = "/KWH/datalogger/transceive/sms/commands/PU03.sh"
PU04Path = "/KWH/datalogger/transceive/sms/commands/PU04.sh"
PU05Path = "/KWH/datalogger/transceive/sms/commands/PU05.sh"
PU06Path = "/KWH/datalogger/transceive/sms/commands/PU06.sh"
PU07Path = "/KWH/datalogger/transceive/sms/commands/PU07.sh"
PU08Path = "/KWH/datalogger/transceive/sms/commands/PU08.sh"

def domainInputCheck(answer):
    while answer != "yes" and answer != "no" and answer != "Yes" and answer != "No" and answer != "n" and answer != "N" and answer != "y" and answer != "Y" and answer !=" ":
        answer = raw_input("Enter a valid answer: yes or no. ")

    if answer == "yes" or answer == "Yes" or answer == " " or answer == "y" or answer == "Y":
        newValue = raw_input(" Enter a new name in the format: www.xxxx.____ fill in the xs. ")
        while not newValue.isalnum():
            newValue = raw_input(" Enter a valid string with letters and/or numbers ")
        ###Run the subrpocess to change the password variable
        

        secondValue = raw_input(" Enter a new name in the format: www.____.xxxx fill in the xs. ")
        while not secondValue.isalnum():
            secondValue = raw_input(" Enter a valid string with letters and/or numbers ")
        ###Run the subrpocess to change the password variable -- NEED A WAY TO LOG WHICH PASS... another parameter??

        newDom = "www."+newValue+"."+secondValue
        print(newDom)

        p = subprocess.Popen([domPath, newDom])

def ApassCheck(answer):
    while answer != "yes" and answer != "no" and answer != "Yes" and answer != "No" and answer != "n" and answer != "N" and answer != "y" and answer != "Y" and answer !=" ":
        answer = raw_input("Enter a valid answer: yes or no. ")

    if answer == "yes" or answer == "Yes" or answer == " " or answer == "y" or answer == "Y":
        newValue = raw_input(" Enter a new value. must be an integer between 0 and 9999. ")
        
        while not newValue.isdigit():
            newValue = raw_input(" Enter a valid integer between 0 and 9999 ")

            #Drop out of loop once you have an integer 
        while  int(newValue) < 0 or int(newValue) >9999:
            newValue = raw_input(" Enter a valid integer between 0 and 9999 ")
        ###Run the subrpocess to change the password variable once all checks are passed 
        p = subprocess.Popen([ApassPath, newValue])

def IpassCheck(answer):
    while answer != "yes" and answer != "no" and answer != "Yes" and answer != "No" and answer != "n" and answer != "N" and answer != "y" and answer != "Y" and answer !=" ":
        answer = raw_input("Enter a valid answer: yes or no. ")

    if answer == "yes" or answer == "Yes" or answer == " " or answer == "y" or answer == "Y":
        newValue = raw_input(" Enter a new value. must be an integer between 0 and 9999. ")
        
        while not newValue.isdigit():
            newValue = raw_input(" Enter a valid integer between 0 and 9999 ")
            
        while int(newValue) < 0 or int(newValue) >9999:
            newValue = raw_input(" Enter a valid integer between 0 and 9999 ")
        ###Run the subrpocess to change the password variable 
        p = subprocess.Popen([IpassPath, newValue])
        
def channelInputCheck(answer, index):
    while answer != "yes" and answer != "no" and answer != "Yes" and answer != "No" and answer != "n" and answer != "N" and answer != "y" and answer != "Y" and answer !=" ":
        answer = raw_input("Enter a valid answer: yes or no. ")

    if answer == "yes" or answer == "Yes" or answer == " " or answer == "y" or answer == "Y":
        newValue = raw_input(" Enter a new value. Choices are 0 or 1 ")
        while not newValue.isdigit():
            newValue = raw_input(" Enter a valid integer: 0 or 1. ")
        while int(newValue) != 0 and int(newValue) != 1:
            newValue = raw_input(" Enter a valid answer: 0 or 1. ")
        ###Run the subrpocess to change the variable
        path = index+"Path"
        print("Path is: " + path)
        if path == "AD01Path":
            p = subprocess.Popen([AD01Path, newValue])
        elif path == "AD02Path":
            p = subprocess.Popen([AD02Path, newValue])
        elif path == "AD03Path":
            p = subprocess.Popen([AD03Path, newValue])
        elif path == "AD04Path":
            p = subprocess.Popen([AD04Path, newValue])
        elif path == "AD05Path":
            p = subprocess.Popen([AD05Path, newValue])
        elif path == "AD06Path":
            p = subprocess.Popen([AD06Path, newValue])
        elif path == "AD07Path":
            p = subprocess.Popen([AD07Path, newValue])
        elif path == "AD08Path":
            p = subprocess.Popen([AD08Path, newValue])
        elif path == "AD09Path":
            p = subprocess.Popen([AD09Path, newValue])
        elif path == "AD10Path":
            p = subprocess.Popen([AD10Path, newValue])
        elif path == "AD11Path":
            p = subprocess.Popen([AD11Path, newValue])
        elif path == "AD12Path":
            p = subprocess.Popen([AD12Path, newValue])
        elif path == "AD13Path":
            p = subprocess.Popen([AD13Path, newValue])
        elif path == "AD14Path":
            p = subprocess.Popen([AD14Path, newValue])
        elif path == "AD15Path":
            p = subprocess.Popen([AD15Path, newValue])
        elif path == "AD16Path":
            p = subprocess.Popen([AD16Path, newValue])
        elif path == "AD17Path":
            p = subprocess.Popen([AD17Path, newValue])
        elif path == "AD18Path":
            p = subprocess.Popen([AD18Path, newValue])

def PchannelInputCheck(answer, index):
    while answer != "yes" and answer != "no" and answer != "Yes" and answer != "No" and answer != "n" and answer != "N" and answer != "y" and answer != "Y" and answer !=" ":
        answer = raw_input("Enter a valid answer: yes or no. ")

    if answer == "yes" or answer == "Yes" or answer == " " or answer == "y" or answer == "Y":
        newValue = raw_input(" Enter a new value. Choices are 0 or 1 ")
        while not newValue.isdigit():
            newValue = raw_input(" Enter a valid integer: 0 or 1. ")
        while int(newValue) != 0 and int(newValue) != 1:
            newValue = raw_input(" Enter a valid answer: 0 or 1. ")
        ###Run the subrpocess to change the variable
        path = index+"Path"
        print("Path is: " + path)
        if path == "PU01Path":
            p = subprocess.Popen([PU01Path, newValue])
        elif path == "PU02Path":
            p = subprocess.Popen([PU02Path, newValue])
        elif path == "PU03Path":
            p = subprocess.Popen([PU03Path, newValue])
        elif path == "PU04Path":
            p = subprocess.Popen([PU04Path, newValue])
        elif path == "PU05Path":
            p = subprocess.Popen([PU05Path, newValue])
        elif path == "PU06Path":
            p = subprocess.Popen([PU06Path, newValue])
        elif path == "PU07Path":
            p = subprocess.Popen([PU07Path, newValue])
        elif path == "PU08Path":
            p = subprocess.Popen([PU08Path, newValue])

            
def portCheck(answer):
    while answer != "yes" and answer != "no" and answer != "Yes" and answer != "No" and answer != "n" and answer != "N" and answer != "y" and answer != "Y" and answer !=" ":
        answer = raw_input("Enter a valid answer: yes or no. ")

    if answer == "yes" or answer == "Yes" or answer == " " or answer == "y" or answer == "Y":
        newValue = raw_input(" Enter a new value. Integer between 0 and 99999 ")
        while not newValue.isdigit():
            newValue = raw_input(" Enter a valid integer between 0 and 9999 ")
        while int(newValue) <= 0 or int(newValue) > 99999:
            newValue = raw_input(" Enter a valid answer: 0 through 99999. ")
        ###Run the subrpocess to change the variable 
    p = subprocess.Popen([portPath, newValue])
        
def apnCheck(answer):
    while answer != "yes" and answer != "no" and answer != "Yes" and answer != "No" and answer != "n" and answer != "N" and answer != "y" and answer != "Y" and answer !=" ":
        answer = raw_input("Enter a valid answer: yes or no. ")

    if answer == "yes" or answer == "Yes" or answer == " " or answer == "y" or answer == "Y":
        newValue = raw_input(" Enter a new APN:  ")
        while not newValue.isdigit():
            newValue = raw_input(" Enter a valid integer between 1 and 99999.  ")
        while int(newValue) < 1 or int(newValue) > 99999:
            newValue = raw_input(" Enter a valid answer: 1 through 99999. ")
        ###Run the subrpocess to change the variable 
        p = subprocess.Popen([apnPath, newValue])

def txCheck(answer):
    while answer != "yes" and answer != "no" and answer != "Yes" and answer != "No" and answer != "n" and answer != "N" and answer != "y" and answer != "Y" and answer !=" ":
        answer = raw_input("Enter a valid answer: yes or no. ")

    if answer == "yes" or answer == "Yes" or answer == " " or answer == "y" or answer == "Y":
        newValue = raw_input(" Enter a new Transmit Interval: 1 through 99999.   ")
        while not newValue.isdigit():
            newValue = raw_input(" Enter a valid integer between 0 and 99999 ")
        while int(newValue) < 0 or int(newValue) > 99999:
            newValue = raw_input(" Enter a valid answer: 1 through 99999. ")
        ###Run the subrpocess to change the variable
        p = subprocess.Popen([txPath, newValue])

def debugCheck(answer):
    while answer != "yes" and answer != "no" and answer != "Yes" and answer != "No" and answer != "n" and answer != "N" and answer != "y" and answer != "Y" and answer !=" ":
        answer = raw_input("Enter a valid answer: yes or no. ")

    if answer == "yes" or answer == "Yes" or answer == " " or answer == "y" or answer == "Y":
        newValue = raw_input(" Enter a new DEBUG value. 0 = OFF, 1 = ON  ")
        while not newValue.isdigit():
            newValue = raw_input(" Enter a valid integer: 0 or 1. ")
        while int(newValue) != 0 and int(newValue) != 1:
            newValue = raw_input(" Enter a valid answer: 0 or 1. ")
        ###Run the subrpocess to change the variable 
        p = subprocess.Popen([debugPath, newValue])

def staCheck(answer):
    while answer != "yes" and answer != "no" and answer != "Yes" and answer != "No" and answer != "n" and answer != "N" and answer != "y" and answer != "Y" and answer !=" ":
        answer = raw_input("Enter a valid answer: yes or no. ")

    if answer == "yes" or answer == "Yes" or answer == " " or answer == "y" or answer == "Y":
        newValue = raw_input(" Enter a new Station Number:  ")
        while not newValue.isdigit():
            newValue = raw_input(" Enter a valid integer between 0 and 9999. ")
        while int(newValue) < 0 or int(newValue) > 99999:
            newValue = raw_input(" Enter a valid answer: 1 through 99999. ")
        ###Run the subrpocess to change the variable
        p = subprocess.Popen([staPath, newValue])


print(" Reconfiguring Administration Password: Valid integers 0 - 9999.")
answer = raw_input(" Administration password set to 1111, do you wish to change this value? ")
ApassCheck(answer)

print(" Reconfiguring Inquiry Password: Valid integers 0 - 9999. ")
answer = raw_input(" Inquiry password set to 0000, do you wish to change this value? ")
IpassCheck(answer)

#AD01 - AD18
print(" Reconfiguring analog channels: 0 = OFF and 1 = ON ")
for item in analogList:
    answer = raw_input(item + " set to 1, do you wish to change this value? ")
    channelInputCheck(answer, item)

#PU01-PU08
print(" Reconfiguring pulse channels: 0 = OFF and 1 = ON ")
for item in pulseList:
    answer = raw_input(item + " set to 1, do you wish to change this value? ")
    PchannelInputCheck(answer, item)

print(" Reconfiguring domain name: ")
answer = raw_input(" Domain name set to: www.kw4h.org do you wish to change this name? ")
domainInputCheck(answer)

print(" Reconfiguring port number: ")
answer = raw_input(" Port number set to: 6001 do you wish to change this name? ")
portCheck(answer)

print(" Reconfiguring port Access Point Name (APN): ")
answer = raw_input(" APN set to: 'internet' do you wish to change this name? ")
apnCheck(answer)


print(" Reconfiguring transmit interval (TX_INTRVL): ")
answer = raw_input(" TX_INTRVL set to: 1, do you wish to change this interval? ")
txCheck(answer)

print(" Reconfiguring debug status (DEBUG) 0 = OFF and 1 = ON: ")
answer = raw_input(" DEBUG set to: 0, do you wish to change this interval? ")
debugCheck(answer)

print(" Reconfiguring debug station number (STA): ")
answer = raw_input(" STA set to: 99999, do you wish to change this value? ")
staCheck(answer)



