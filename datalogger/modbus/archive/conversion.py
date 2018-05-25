#!/usr/bin/env python
# Takes in command line arguments
# start bit, stop bit, parity bit, data(HEX)
# Could just pad with 0s... depending on how to HEX conversion happens
# converts to binary
# flips the bits
# adds the start bit on at the beginning
# adds the parity bit on at the end
# adds the end bit on the end of that
# convert to hex -- keep an eye on this
# converts to decimal (starting from left and moving to right)

import sys

startBit, stopBit, parityBit, data = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
def convert():

#NOTEs: 
#
# Carrie had written this shell to take in arguments and use them like I had asked for, 
# so I appended your code to the bottom and modified it slightly to make them work togethor
# the usage is now: > ./conversion.py <start> <stop> <parity> <hex_data>
# e.g. > ./conversion.py 0 0 0 0101
#
# Start bit and stop bit can only be 0 or 1, but
# parityBit should have 5 options 0-4 -
#	0: Parity bit = 0
#	1: Parity bit = 1
#	2: Parity bit is even parity
#	3: Parity bit is odd parity
#	4: No parity bit
# Even parity means that if the the number of ones in the byte is even, the parity bit is 1,
# if it is odd, the parity bit is 0
# Odd parity is the opposite, if the number of 1 bits in the byte is odd, the parity bit is 1, if the number
# is even the parity bit is 0.
# Google this to confirm I don't have them backwards
# 

    print(startBit, stopBit, parityBit, data)
    print(bin(int(data,16)))

    begin = "" #28 0 bits 
    #begin = "0000000000000000000000000000" #28 0 bits 
    end = "" # 28 0 bits 
    #end = "00000000000000000000000000" # 28 0 bits 

    def binary(n):
	return '{0:08b}'.format(n) #converts int to bin 

    def hex2dec2bin(myinput): #converts hex to bin
	#adds the start buffer
	modbusMsg = begin
	
	length = len(myinput)
	#print (length)
	
	for i in range (0, length):
            #print(myinput[i])
	    input1 = myinput[i]
	    hexint = int(input1,16) #turns hex into decimal
	    #print(hexint) print(binary(hexint)) 
	    #print(binary(hexint)[::-1]) #flips the bits 
	    #startBit+8_bit_msg+stopBit msg = startBit + 
	    #binary(hexint) + stopBit
	    msg = startBit + binary(hexint)[::-1] + stopBit
	    #startBit+8_bit_msg+parityBit+stopBit msg = 
	    #startBit + binary(hexint) + parityBit + stopBit 
	    #msg = startBit + binary(hexint)[::-1] + 
	    #parityBit + stopBit creates the modbus message
	    modbusMsg = modbusMsg + msg
	
	#adds the 0 buffer
	modbusMsg = modbusMsg + end
	
	print modbusMsg
	return modbusMsg

    #input2 = "123A"
    hex2dec2bin(data)

convert()
