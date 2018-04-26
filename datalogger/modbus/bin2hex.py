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
def convert():
    if int(parityBit) == 4:
        #buffer = 35
        parityBit = 0   #means there is no parity bit
        buffer = 0
    else:
        #buffer = 39
        parityBit = 1 #means there is a parity bit
        buffer = 0    
    
    #start_bit = 1 #1 indicate there is a start bit stop_bit = 1 #1 
    #indicates there is a stop bit parity_bit = 0 #0 indicates there is 
    #no parity bit
    def trim(myinput, num): #this function removes the start, stop, and parity
        myinput = myinput[num::]
        myinput = myinput[::-1]
        myinput = myinput[num + int(parityBit)::]
        myinput = myinput[::-1]
        return myinput

    def parse(myinput, num): #this function removes the inital buffer
        myinput = myinput[num::]
        myinput = myinput[::-1]
        myinput = myinput[num::]
        myinput = myinput[::-1]
        return myinput

    def split(myinput): #this function converts the binary data to hex
        hexstr = ""
        inputA = str(hex(int(myinput[0:4][::-1],2))[2::])
        inputB = str(hex(int(myinput[4:8][::-1],2))[2::])
        hexstr = inputA + inputB
        return hexstr

    def bin2dec2hex(myinput): #converts bin to hex
        bits = 10 + int(parityBit)
        hexstr = ""
        modmsg = parse(myinput, buffer)
        length = len(modmsg)
        leng = (length+1)/bits
        for i in range (1, leng):
            part = trim(modmsg[i+bits:(i+1)*bits], int(startBit))
            hexstr = hexstr + split(part)
        #print(hexstr)
        return hexstr

    #print(startBit, stopBit, parityBit, data)
    output = bin2dec2hex(data)
    length = len(output)
    return output
print convert()
