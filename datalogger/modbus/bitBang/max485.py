#!/usr/bin/env python

import pigpio
import time
pi = pigpio.pi()
if not pi.connected:
	exit()


#This assumes that the data direction pin on the MAX485 is connected to
#GPIO pin 9 on the RPi and sets toggles the pin high and low. The user should
# be able to see the transmitting pin the MAX485 change from 0 to 5V


pi.set_mode(9, pigio.OUTPUT) #GPIO 9 as input
while(1):
	pi.write(9, 0)
	print(pi.read(9))
	time.sleep(5)
	pi.write(9,1)
	print(pi.read(9))		

pi.stop()
