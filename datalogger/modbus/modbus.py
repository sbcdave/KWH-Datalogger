#!/usr/bin/env python
import minimalmodbus

minimalmodbus.BAUDRATE = 9600
minimalmodbus.PARITY = 'N'
minimalmodbus.BYTESIZE = 8
minimalmodbus.STOPBITS = 1
minimalmodbus.TIMEOUT = 0.05
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = False

BUS = minimalmodbus.Instrument('/dev/spidev0.0', 1, 'MODE_RTU')
BUS.debug = True

test = BUS.read_register(289, 1)
print(test)

