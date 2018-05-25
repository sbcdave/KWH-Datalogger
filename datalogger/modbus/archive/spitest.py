#!/usr/bin/env python
import wiringpi
import thread
import time 

def send( ):
    SPIchannel = 0 #SPI Channel (CE0)
    SPIspeed = 4800 #Clock Speed in Hz
    wiringpi.wiringPiSetupGpio()
    wiringpi.wiringPiSPISetup(SPIchannel, SPIspeed)
    sendData = chr(170)+chr(170)+chr(170)+chr(170)+chr(170)+chr(170)+chr(170)\
    +chr(170)+chr(170)+chr(170)+chr(170)+chr(170)+chr(170)+chr(170)+chr(170)\
    +chr(170)+chr(170)+chr(170)
    recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)
    print recvData

#config
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
TxEnable = 2
io.pinMode(TxEnable,io.OUTPUT)
io.digitalWrite(TxEnable,io.HIGH)
thread.start_new_thread( send, () )
time.sleep(.03)
io.digitalWrite(TxEnable,io.LOW)


#alternatively, to send a single byte:

#recvData is again a list e.g. [1, '\x9A']
