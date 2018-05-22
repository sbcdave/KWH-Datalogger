#!/usr/bin/env python
# Takes in command line arguments parityBit is cause for the parity 
# bit (even, odd, 0, 1, none start bit, stop bit, parity bit, 
# data(HEX) Could just pad with 0s... depending on how to HEX 
# conversion happens converts to binary flips the bits adds the 
# start bit on at the beginning adds the parity bit on at the end 
# adds the end bit on the end of that convert to hex -- keep an eye 
# on this converts to decimal (starting from left and moving to 
# right)
import sys 
startBit, stopBit, parityBit, data = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] 

def convert():    
    # Note that it says at least 3.5 character lengths, and that we 
    # may want a variable called character length, that is 
    # calculated by the input arguments (i.e. 10 or 11) and then 
    # the number of 0's is calculated as 3.5 times the charactler 
    # length, rounding up.
    
#    print(startBit, stopBit, parityBit, data)
#    print(bin(int(data,16)))

    if int(parityBit) == 4:
        begin = "" #28 0 bits
#        begin = "00000000000000000000000000000000000" #35 0 bits
        end = "" # 28 0 bits
#        end = "00000000000000000000000000000000000" # 35 0 bits
    else:
        begin = "" #28 0 bits
#        begin = "000000000000000000000000000000000000000" #39 0 bits
        end = "" # 28 0 bits
#        end = "000000000000000000000000000000000000000" # 39 0 bits	
    
    def binary(n):
        return '{0:04b}'.format(n) #converts int to bin
    
    def parity_func(input, parityBit):
        count = 0
        #print("input:", input)
        length = len(input)
        for i in range (0, length):
            if (input[i] == "1"):
                count = count + 1
        #print("count:", count)
        if(parityBit == "2"):
            #even parity
            if (count % 2 == 0):
                parityBit = "0"
            else:
                parityBit = "1"
        elif(parityBit == "3"):
            #odd parity
            if (count % 2 == 0):
                parityBit = "1"
            else:
                parityBit = "0"
        elif(parityBit == "0"):
            parityBit = "0"
        elif(parityBit == "1"):
            parityBit = "1"
        else:
            parityBit = "0"
        #print("parityBit:", parityBit)
        return parityBit

    def hex2dec2bin(myinput): #converts hex to bin
        #adds the start buffer
        modbusMsg = begin
    
        length = len(myinput)
        #print (length)
    
        for i in range (0, length):
            if (i % 2 == 0):
                input1 = myinput[i]
                input2 = myinput[i+1]
                hexint1 = int(input1,16) #turns hex into decimal
                hexint2 = int(input2,16)
                parity_bit = parity_func(binary(hexint1) + binary(hexint2), parityBit)
                if(parityBit == "4"):
                    #startBit+8_bit_msg+stopBit 
                    #msg = startBit + binary(hexint2) + binary(hexint1) + stopBit
                    msg = startBit + binary(hexint2)[::-1] + binary(hexint1)[::-1] + stopBit
                else:
                    #startBit+8_bit_msg+parityBit+stopBit 
                    #msg = startBit + binary(hexint2) +binary(hexint1) + parity_bit + stopBit
                    msg = startBit + binary(hexint2)[::-1] + binary(hexint1)[::-1] + parity_bit + stopBit
                
                #creates the modbus message
                modbusMsg = modbusMsg + msg
    
        #adds the 0 buffer
        modbusMsg = modbusMsg + end
    
        return modbusMsg
    
    output = hex2dec2bin(data)
    length = len(output)
    return output
    
print convert()

