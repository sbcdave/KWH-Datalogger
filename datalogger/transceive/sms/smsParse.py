#!/usr/bin/env python


import sys
import string

fileName = open('read.txt', "r")

useful = []

#Read in line by line
for line in fileName:
    lineIn = line.split()
    count  = 0 
    for element in lineIn:
        count = count + 1
    if count != 0:
        useful.append(lineIn)

keep = []
parsing = []
for item in useful:
    if item[0] == "+CMGL:":
        parsing.append(item)
    else:
        keep.append(item)

phoneNumbers = []
messageNumbers = []
messages = []

#print(keep)

messages = keep[4::]

for item in parsing:
    messageNumbers.append(item[1])
    phoneNumbers.append(item[2])

#Lists will keep the order, so
# if you need to access a certain element
# you can access by element number

mn = ""
messNum = []
for item in messageNumbers:
    for char in item:
        #print(char)
        if char == "'":
            #do nothing
            #Skip this one
            print(" Nothing ")
        if char == ',':
            break
        else:
            messNum.append(char)

print("\n")
#FINAL LIST OF MESSAGE NUMBERS
print("Message Numbers: ", messNum)

#Now finish parsing the phone numbers
phoneNums = []
for item in phoneNumbers:
    phoneNums.append(item[8:20])

print("\n")
#FINAL LIST OF PHONE NUMBERS        
print("Phone Numbers: ", phoneNums)        

print("\n")
#FINAL LIST OF MESSAGES
print("Messages", messages)

print("\n")                      

