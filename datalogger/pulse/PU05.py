#!/usr/bin/env python

# tally.py

import time

import pigpio

pi = pigpio.pi()

if not pi.connected:
    exit()

DIN=19

pi.set_mode(DIN, pigpio.INPUT)
pi.set_pull_up_down(DIN, pigpio.PUD_DOWN)

pulse_cb = pi.callback(DIN, pigpio.RISING_EDGE)

while True:

   time.sleep(5)

   with open("/KWH/datalogger/pulse/PU05", 'w') as PU05:
      PU05.write(str(pulse_cb.tally()))

pi.stop()
