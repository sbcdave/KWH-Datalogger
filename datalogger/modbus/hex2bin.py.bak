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
# Carrie had written this shell of code to take in arguments and use them like I had asked, 
# so I appended your code to the bottom and modified it slightly to make take advantage
# of the argument input
#
# in a linux environment, the usage is: > ./conversion.py <start> <stop> <parity> <hex_data>
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
# In hex, a byte is two hex characters: e.g. 01 = 0000 0001, FF = 1111 1111
# So each hex character is equivalent to 4 bits that range from 0-15 i.e. 0-F
# The code currently treats each hex character as 8 bits. From the looks of it you
# will need consume a second character in the for loop to decide on the 8 bits
# that should be flipped, per byte.
#
# Also note that in modbus language a "character" is the byte + the extra bits
# e.g. the byte 01 in modbus language is represented by the modbus character
# x10000000ps where x is the start bit, 10000000 is the reversed byte, p is
# the parity bit, and s is the stop bit.
# The importance of this character is that if the parity bit is off, the character
# length is 10 bits, otherwise, it is 11 bits.
# I see that you chose 28 0's for the begin and end, I'm assuming you got that
# from the 3.5 character lengths, but were assuming a character was 8 bits.
# Note that it says at least 3.5 character lengths, and that we may want a
# variable called character length, that is calculated by the input arguments
# (i.e. 10 or 11) and then the number of 0's is calculated as 3.5 times the
# charactler length, rounding up.
#
# Good work!

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
