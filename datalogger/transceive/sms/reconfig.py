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



def domainInputCheck(answer):
    while answer != "yes" and answer != "no" and answer != "Yes" and answer != "No":
        answer = raw_input("Enter a valid answer: yes or no. ")

    if answer == "yes" or answer == "Yes":
        newValue = raw_input(" Enter a new name in the format: www.xxxx.____ fill in the xs. ")
        while not newValue.isalnum():
            newValue = raw_input(" Enter a valid string with letters and/or numbers ")
        ###Run the subrpocess to change the password variable -- NEED A WAY TO LOG WHICH PASS... another parameter??

        secondValue = raw_input(" Enter a new name in the format: www.____.xxxx fill in the xs. ")
        while not secondValue.isalnum():
            secondValue = raw_input(" Enter a valid string with letters and/or numbers ")
        ###Run the subrpocess to change the password variable -- NEED A WAY TO LOG WHICH PASS... another parameter??

        newDom = "www."+newValue+"."+secondValue
        print(newDom)


def passCheck(answer):
    while answer != "yes" and answer != "no" and answer != "Yes" and answer != "No":
        answer = raw_input("Enter a valid answer: yes or no. ")

    if answer == "yes" or answer == "Yes":
        newValue = raw_input(" Enter a new value. must be an integer between 0 and 9999. ")
        while int(newValue) < 0 or int(newValue) >9999:
            newValue = raw_input(" Enter a valid integer between 0 and 9999 ")
        ###Run the subrpocess to change the password variable -- NEED A WAY TO LOG WHICH PASS... another parameter??

def channelInputCheck(answer):
    while answer != "yes" and answer != "no" and answer != "Yes" and answer != "No":
        answer = raw_input("Enter a valid answer: yes or no. ")

    if answer == "yes" or answer == "Yes":
        newValue = raw_input(" Enter a new value. Choices are 0 or 1 ")
        while int(newValue) != 0 and int(newValue) != 1:
            newValue = raw_input(" Enter a valid answer: 0 or 1. ")
        ###Run the subrpocess to change the variable -- Need a way to log which channel... another parameter??


def portCheck(answer):
    while answer != "yes" and answer != "no" and answer != "Yes" and answer != "No":
        answer = raw_input("Enter a valid answer: yes or no. ")

    if answer == "yes" or answer == "Yes":
        newValue = raw_input(" Enter a new value. Integer between 1 and 99999 ")
        while int(newValue) <= 0 or int(newValue) > 99999:
            newValue = raw_input(" Enter a valid answer: 1 through 99999. ")
        ###Run the subrpocess to change the variable -- Need a way to log which channel... another parameter??

def apnCheck(answer):
    while answer != "yes" and answer != "no" and answer != "Yes" and answer != "No":
        answer = raw_input("Enter a valid answer: yes or no. ")

    if answer == "yes" or answer == "Yes":
        newValue = raw_input(" Enter a new value. Integer between 1 and 99999 ")
    if answer == "yes" or answer == "Yes":
        newValue = raw_input(" Enter a new APN:  ")
        while not newValue.isalnum():
            newValue = raw_input(" Enter a valid string with letters and/or numbers ")

            newValue = raw_input(" Enter a valid answer: 1 through 99999. ")
        ###Run the subrpocess to change the variable -- Need a way to log which channel... another parameter??


        

print(" Reconfiguring Administration Password: Valid integers 0 - 9999.")
answer = raw_input(" Administration password set to 1111, do you wish to change this value? ")
passCheck(answer)

print(" Reconfiguring Inquiry Password: Valid integers 0 - 9999. ")
answer = raw_input(" Inquiry password set to 0000, do you wish to change this value? ")
passCheck(answer)

print(" Reconfiguring analog channels: 0 = OFF and 1 = ON ")
for item in analogList:
    answer = raw_input(item + " set to 1, do you wish to change this value? ")
    channelInputCheck(answer)

print(" Reconfiguring pulse channels: 0 = OFF and 1 = ON ")
for item in pulseList:
    answer = raw_input(item + " set to 1, do you wish to change this value? ")
    channelInputCheck(answer)

print(" Reconfiguring domain name: ")
answer = raw_input(" Domain name set to: www.kw4h.org do you wish to change this name? ")
domainInputCheck(answer)

print(" Reconfiguring port number: ")
answer = raw_input(" Port number set to: 6001 do you wish to change this name? ")
portCheck(answer)

print(" Reconfiguring port Access Point Name (APN): ")
answer = raw_input(" APN set to: 'internet' do you wish to change this name? ")
apnCheck(answer)
