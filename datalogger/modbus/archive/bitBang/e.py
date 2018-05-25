#!/usr/bin/env python
from __future__ import print_function
import wiringpi
from time import sleep

#config
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
MISO = 13
MOSI = 12
TxEnable = 2
baud_interval = 0.0001395
frame_delay = 0.016041666666666666
#frame_delay = 0.014583333333333334
io.pinMode(TxEnable,io.OUTPUT)
io.pinMode(MOSI,io.OUTPUT)
io.pinMode(MISO,io.INPUT)


#prep MOSI LOW
io.digitalWrite(MOSI,io.HIGH)

#create rising edge and send ":" to signal tx
io.digitalWrite(TxEnable,io.LOW)
sleep(0.1)
io.digitalWrite(TxEnable,io.HIGH)
sleep(frame_delay)

#WRITE
#byte 1 - Address
#1 Start Bit
io.digitalWrite(MOSI,io.LOW)
sleep(baud_interval)
#2 Least Significant
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)
#3
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#4
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#5
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#6
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#7
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#8
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#9 Most Significant
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#Might want parity bit here
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)
#10 Stop Bit
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)


#byte 2 - Function Code
#1 Start Bit
io.digitalWrite(MOSI,io.LOW)
sleep(baud_interval)
#2 Least Significant
io.digitalWrite(MOSI,io.LOW)
sleep(baud_interval)
#3
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#4
io.digitalWrite(MOSI,io.HIGH)     
sleep(baud_interval)
#5
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#6
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#7
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#8
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#9 Most Significant
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#Might want parity bit here
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)
#10 Stop Bit
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)


#byte 3 - Start Address HIGH
#1 Start Bit
io.digitalWrite(MOSI,io.LOW)
sleep(baud_interval)
#2 Least Significant
io.digitalWrite(MOSI,io.LOW)
sleep(baud_interval)
#3
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#4
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#5
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#6
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#7
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#8
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#9 Most Significant
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#Might want parity bit here
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)
#10 Stop Bit
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)

#byte 4 - Start Address LOW
#1 Start Bit
io.digitalWrite(MOSI,io.LOW)
sleep(baud_interval)
#2 Least Significant
io.digitalWrite(MOSI,io.LOW)
sleep(baud_interval)
#3
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#4
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#5
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#6
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#7
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#8
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#9 Most Significant
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#Might want parity bit here
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)
#10 Stop Bit
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)

#byte 5 - Number of registers HIGH
#1 Start Bit
io.digitalWrite(MOSI,io.LOW)
sleep(baud_interval)
#2 Least Significant
io.digitalWrite(MOSI,io.LOW)
sleep(baud_interval)
#3
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#4
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#5
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#6
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#7
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#8
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#9 Most Significant
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#Might want parity bit here
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)
#10 Stop Bit
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)

#byte 6 - Number of registers LOW
#1 Start Bit
io.digitalWrite(MOSI,io.LOW)
sleep(baud_interval)
#2 Least Significant
io.digitalWrite(MOSI,io.LOW)
sleep(baud_interval)
#3
io.digitalWrite(MOSI,io.HIGH)     
sleep(baud_interval)
#4
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#5
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#6
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#7
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#8
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#9 Most Significant
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#Might want parity bit here
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)
#10 Stop Bit
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)

#byte 7 - Error Check LOW
#1 Start Bit
io.digitalWrite(MOSI,io.LOW)
sleep(baud_interval)
#2 Least Significant
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)
#3
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#4
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#5
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#6
io.digitalWrite(MOSI,io.HIGH)     
sleep(baud_interval)
#7
io.digitalWrite(MOSI,io.HIGH)     
sleep(baud_interval)
#8
io.digitalWrite(MOSI,io.HIGH)     
sleep(baud_interval)
#9 Most Significant
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#Might want parity bit here
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)
#10 Stop Bit
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)

#byte 8 - Error Check HIGH
#1 Start Bit
io.digitalWrite(MOSI,io.LOW)
sleep(baud_interval)
#2 Least Significant
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)
#3
io.digitalWrite(MOSI,io.HIGH)     
sleep(baud_interval)
#4
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#5
io.digitalWrite(MOSI,io.HIGH)     
sleep(baud_interval)
#6
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#7
io.digitalWrite(MOSI,io.LOW)     
sleep(baud_interval)
#8
io.digitalWrite(MOSI,io.HIGH)     
sleep(baud_interval)
#9 Most Significant
io.digitalWrite(MOSI,io.HIGH)     
sleep(baud_interval)
#Might want parity bit here
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)
#10 Stop Bit
io.digitalWrite(MOSI,io.HIGH)
sleep(baud_interval)


sleep(frame_delay)
io.digitalWrite(TxEnable,io.LOW)


#READ
#byte 1
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(" ", end=" ")

#byte 2
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(" ", end=" ")

#byte 3
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(" ", end=" ")

#byte 4
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(" ", end=" ")

#byte 5
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(" ", end=" ")

#byte 6
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(" ", end=" ")

#byte 7
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(" ", end=" ")

#byte 8
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(io.digitalRead(MISO), end="")
sleep(baud_interval)
print(" ")
