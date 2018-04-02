#!/usr/bin/env python


#Takes in command line arguments
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
import string
import binascii 

startBit, stopBit, parityBit, data = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
def convert():

    
    print(startBit, stopBit, parityBit, data)
    print(bin(int(data,16)))
convert()
