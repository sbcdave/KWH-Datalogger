#!/usr/bin/env python
import wiringpi
from time import sleep

def write(cmd):
    io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)

    MISO = 13
    MOSI = 12
    TxEnable = 2

    io.pinMode(TxEnable,io.OUTPUT)
    io.pinMode(MOSI,io.OUTPUT)
    io.pinMode(MISO,io.INPUT)

    while cmd != 0:
	if (cmd & 0x01):
#	    io.digitalWrite(MOSI,io.HIGH)
            print(1)
            cmd = cmd >> 1
	    sleep(0.000833333)
        else:
#	    io.digitalWrite(MOSI,io.LOW)     
            print(0)
            cmd = cmd >> 1
	    sleep(0.000833333)
     
#    commandout = adcnum
#    commandout |= 0xFFFFFFFFFFFFFFFF  # start bit + single-ended bit

#    for i in range(16):
#    while True:
#        GPIO.output(MOSI, True)
#        GPIO.output(MOSI, False)

     
#    adcout = 0
    # read in one empty bit, one null bit and 12 ADC bits
#    for i in range(14):
#        GPIO.output(CLK, True)
#        GPIO.output(CLK, False)
#        adcout <<= 1
#        if (GPIO.input(MISO)):
#            adcout |= 0x1
     
#    GPIO.output(CS, True)
            
#    adcout >>= 1       # first bit is 'null' so drop it
#    return adcout

write(9999999999999)
