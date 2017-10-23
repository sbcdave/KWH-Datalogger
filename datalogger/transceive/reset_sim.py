#!/usr/bin/env python
import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(12, gpio.OUT, initial=gpio.LOW)

gpio.output(12, gpio.HIGH)
sleep(3)
gpio.output(12, gpio.LOW)
sleep(1)
