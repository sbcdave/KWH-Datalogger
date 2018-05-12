#!/usr/bin/env python

# tally.py

import time

import pigpio

pi = pigpio.pi()

if not pi.connected:
    exit()

DIN=20

pi.set_mode(DIN, pigpio.INPUT)
pi.set_pull_up_down(DIN, pigpio.PUD_DOWN)

pulse_cb = pi.callback(DIN, pigpio.RISING_EDGE)

PU02 = open("/KWH/datalogger/pulse/PU02", 'r')
previous = int(PU02.read())
PU02.close()

while True:

   time.sleep(5)

   new = pulse_cb.tally()
   current = previous + new
   PU02 = open("/KWH/datalogger/pulse/PU02", 'w')
   PU02.write(str(current))
   PU02.close()

pi.stop()
