#!/usr/bin/env python
import wiringpi
import thread
import time 
import sys

def send( ):
    SPIchannel = 0 #SPI Channel (CE0)
    SPIspeed = 2400 #Clock Speed in Hz
    wiringpi.wiringPiSetupGpio()
    wiringpi.wiringPiSPISetup(SPIchannel, SPIspeed)
    sendData = sys.argv[1]
#    sendData = chr(0)+chr(64)+chr(16)+chr(4)+chr(1)+chr(64)+chr(68)\
#    +chr(16)+chr(4)+chr(1)+chr(0)+chr(72)+chr(20)+chr(116)+chr(123)\
#    +chr(0)+chr(64)+chr(16)+chr(4)+chr(1) 
    recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)
    print recvData

#0 64 16 4 1
#64 68 16 4 1
#0 72 20 116 123
#0 64 16 4 1

#config
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
TxEnable = 2
io.pinMode(TxEnable,io.OUTPUT)
io.digitalWrite(TxEnable,io.HIGH)
thread.start_new_thread( send, () )
time.sleep(.066666)
io.digitalWrite(TxEnable,io.LOW)


#alternatively, to send a single byte:

#recvData is again a list e.g. [1, '\x9A']
