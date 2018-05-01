#!/usr/bin/env python
import wiringpi
import spidev
import time 
import sys

# you can execute this in bash with ./spid.py
# you can execute other things and feed their output as an argument into another program like this
# ./program1 $(./program2)
# for our example here's one option:
# ./spid.py $(./hex2bin.py 1 0 0 01040000000271BC)
# 01040000000271BC is the request for voltage from modbus with address 1
# we can try switching this up, and or decoding the output that comes back
# another potentially useful execution
# ./bin2hex.py 1 0 0 $(./spid.py $(./hex2bin.py 1 0 0 01040000000271BC))
#config spi
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 2400
#spi.mode = 0b00
#spi.loop = True

#config R/W toggle pin
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
TxEnable = 2
io.pinMode(TxEnable,io.OUTPUT)

#send
io.digitalWrite(TxEnable,io.HIGH)

sendData = int(sys.argv[1])
#sendData = [0,64,16,4,1,64,69,16,4,1,0,72,20,116,123\
#,0,64,16,4,1]

spi.writebytes([sendData])

#receive
time.sleep(.001)
io.digitalWrite(TxEnable,io.LOW)

recvData = spi.readbytes(300)
#recvData = [0]*166
#spi.xfer(recvData)

print ''.join('{:02b}'.format(x) for x in recvData)
