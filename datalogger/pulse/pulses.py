#!/usr/bin/env python

# tally.py

import time

import pigpio

pi = pigpio.pi()

if not pi.connected:
    exit()

DI1=26

pi.set_mode(DI1, pigpio.INPUT)
pi.set_pull_up_down(DI1, pigpio.PUD_DOWN)

pulse_cb = pi.callback(DI1, pigpio.RISING_EDGE)

while True:

   time.sleep(5)

   with open("/KWH/datalogger/pulse/PU04", 'w') as PU04:
      PU04.write(str(pulse_cb.tally()))

pi.stop()
