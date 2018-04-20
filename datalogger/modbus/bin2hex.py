#!/usr/bin/env python
# Takes in command line arguments start bit, stop bit, parity bit, 
# data(BIN) the start bit, stop bit, and parity bit value represent 
# is there is one. ie. startBit = 1 means there is a start bit. 
# Could just pad with 0s... depending on how to HEX conversion 
# happens Removes the beginning and ending buffer from the 
# data(BIN) Parses through the data(BIN) Converts to hex returns 
# the hex representation of the data
import sys 
startBit, stopBit, parityBit, data = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

if int(parityBit) == 4:
    #buffer = 35
    buffer = 0
else:
    #buffer = 39
    buffer = 0    
    
#start_bit = 1 #1 indicate there is a start bit stop_bit = 1 #1 
#indicates there is a stop bit parity_bit = 0 #0 indicates there is 
#no parity bit
def trim(myinput, num): #this function removes the intial buffer
    myinput = myinput[num::]
    myinput = myinput[::-1]
    myinput = myinput[num + int(parityBit)::]
    myinput = myinput[::-1]
    return myinput

def parse(myinput, begin, end): #this function removes the startBit, stopBit, and parityBit
    myinput = myinput[begin:end]
    myinput = trim(myinput, start_bit)
    return myinput

def split(myinput): #this function converts the binary data to hex
    hexstr = ""
    inputA = str(hex(int(myinput[0:4],2)))[2::]
    inputB = str(hex(int(myinput[4:8],2)))[2::]
    #print(inputA, inputB)
    hexstr = inputA + inputB
    return hexstr

def bin2dec2hex(myinput): #converts bin to hex
    hexstr = ""
    #print(myinput)
    modmsg = trim(myinput, buffer)
    #print(modmsg)
    length = len(modmsg)
    #print (length)
    for i in range (1, length+1):
        if (i % 10 == 0):
            part = parse(modmsg, i-10, i)
            #print (part)
            hexstr = hexstr + split(part)
    print(hexstr)
    return hexstr

print(startBit, stopBit, parityBit, data)
bin2dec2hex(data)
