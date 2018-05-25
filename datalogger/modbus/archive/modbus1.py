#!/usr/bin/python
import minimalmodbus
import serial
import pigpio
import time

pi = pigpio.pi()
if not connected
exit()

pi.set_mode(9, pigpio.OUTPUT)

#import pyserial
instrument = minimalmodbus.Instrument('/dev/spidev0.0', 1)

#instr.debug = True

instrument.serial.port
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 0.5
instrument.address
instrument.mode = minimalmodbus.MODE_RTU



def read_meter():
    #print (instrument)
    #read = instrument.write_register(1,1)
    read = instrument.read_register(1, 0, 3, true)
    value = instrument.read_float(1)
    print (read)
    #file = open('/KWH/datalogger/modbus/modbus.txt', 'w+')
    #file.write('{} {}\n'.format(read, value))
    #file.close()

def main():
    while(1):
        pi.write(9,1)
        time.sleep(1)
        read_meter()
        time.sleep(1)
        pi.write(9,0)

if __name__ == "__main__":
    main()
