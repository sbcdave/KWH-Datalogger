#!/usr/bin/python
import minimalmodbus as m

inst = m.Instrument('/dev/spidev0.0', 1)
inst.serial.baudrate = 9600

test = inst.read_register(289, 1)
print(test)

