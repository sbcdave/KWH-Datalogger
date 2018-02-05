#!/usr/bin/env python

import pigpio

pi = pigpio.pi()
if not pi.connected:
	exit()

pi.set_mode(9, pigio.OUTPUT) #GPIO 9 as input
while(1):
	pi.write(9, 0)
	print(pi.read(9))
	
	pi.write(9,1)
	print(pi.read(9))		

pi.stop()
