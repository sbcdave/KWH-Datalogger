#!/usr/bin/env python
import time
import sys
import serial
import os

log = open('/KWH/datalogger/transceive/tcp.log', 'a+')
log.write('Starting TCP transmission\n')

sim = serial.Serial('/dev/ttyAMA0', 115200, timeout=5)
sim.flushInput()
sim.flushOutput()

print "AT+CIPSHUT"
sim.write('AT+CIPSHUT')
bytesToRead = sim.inWaiting()
resp = sim.read(bytesToRead)
log.write(resp)

print "AT+CGATT=0"
sim.write('AT+CGATT=0')
bytesToRead = sim.inWaiting()
resp = sim.read(bytesToRead)
log.write(resp)

sim.write('AT+CGATT=1')
bytesToRead = sim.inWaiting()
resp = sim.read(bytesToRead)
log.write(resp)

sim.write('AT+CIPSHUT')
bytesToRead = sim.inWaiting()
resp = sim.read(bytesToRead)
log.write(resp)

sim.write('AT+CIPMUX=0')
bytesToRead = sim.inWaiting()
resp = sim.read(bytesToRead)
log.write(resp)

sim.write('AT+CSTT="wholsale"')
bytesToRead = sim.inWaiting()
resp = sim.read(bytesToRead)
log.write(resp)

sim.write('AT+CIICR')
bytesToRead = sim.inWaiting()
resp = sim.read(bytesToRead)
log.write(resp)

sim.write('AT+CIFSR')
bytesToRead = sim.inWaiting()
resp = sim.read(bytesToRead)
log.write(resp)


print 'AT+CIPSTART="TCP","'+os.environ["DOMAIN"]+'","'+os.environ["PORT"]+'"'
sim.write('AT+CIPSTART="TCP","'+os.environ["DOMAIN"]+'","'+os.environ["PORT"]+'"')
bytesToRead = sim.inWaiting()
resp = sim.read(bytesToRead)
log.write(resp)

sim.write('AT+CIPSEND')
bytesToRead = sim.inWaiting()
resp = sim.read(bytesToRead)
log.write(resp)

with open('/KWH/datalogger/transceive/tcp/tstring', 'r') as tstring:
    sim.write(tstring.read())
bytesToRead = sim.inWaiting()
resp = sim.read(bytesToRead)
log.write(resp)

sim.write('AT+CIPCLOSE')
bytesToRead = sim.inWaiting()
resp = sim.read(bytesToRead)
log.write(resp)

sim.write('AT+CIPSHUT')
bytesToRead = sim.inWaiting()
resp = sim.read(bytesToRead)
log.write(resp)
