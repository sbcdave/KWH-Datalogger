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

while True:

   time.sleep(5)

   with open("/KWH/datalogger/pulse/PU02", 'w') as PU02:
      PU02.write(str(pulse_cb.tally()))

pi.stop()
