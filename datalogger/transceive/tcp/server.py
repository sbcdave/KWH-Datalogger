#!/usr/bin/env python
import socket
import time
import signal
import sys
import serial

def signal_handler(signal, frame):
        print('Closing SIM Server')
        log.close()
        sim.close()
        s.close()
        cs.close()
        exit(0)
signal.signal(signal.SIGINT, signal_handler)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 9999
s.bind((host, port))
s.listen(10)
sim=serial.Serial('/dev/ttyAMA0', 115200, timeout=5)
sim.flushInput()
sim.flushOutput()
while True:
    cs,addr = s.accept()
    data=cs.recv(1024)
    sim.write(data)
    bytesToRead = sim.inWaiting()
    resp=sim.read(bytesToRead)
    with open("/KWH/datalogger/transceive/tcp/test.log", "a") as log:
	log.write(resp)
    cs.close()
