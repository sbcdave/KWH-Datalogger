#!/usr/bin/env python
import socket
import time
import signal
import sys
import serial
import os

def signal_handler(signal, frame):
        log.write('Closing SIM Server\n')
        log.close()
        sim.close()
        comslog.close()
	s.close()
        cs.close()
        exit(0)
signal.signal(signal.SIGINT, signal_handler)

log = open("/KWH/datalogger/transceive/simServer.log", "w")
log.write("Starting SIM Server\n")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 9999
port_chosen = False

log.write("Starting port selection\n")
while not port_chosen:
    try:
	s.bind((host, port))
        port_chosen = True
    except:
	log.write("Port "+str(port)+" in use\n")
	port = port + 1

log.write("Port "+str(port)+" selected\n")
os.environ["SIM_PORT"] = str(port)
log.write("SIM_PORT: "+os.environ["SIM_PORT"]+"\n")
log.write("Listening...\n")
log.close()
s.listen(100)
sim = serial.Serial('/dev/ttyAMA0', 115200, timeout=5)
sim.flushInput()
sim.flushOutput()
while True:
    cs,addr = s.accept()
    with open("/KWH/datalogger/transceive/simServer.log", "a") as log:
	log.write("accepted: "+str(addr)+"\n")
    data = cs.recv(1024)
    with open("/KWH/datalogger/transceive/simServer.log", "a") as log:
        log.write("received: "+data+"\n")
    sim.write(data)
    with open("/KWH/datalogger/transceive/simServer.log", "a") as log:
        log.write("wrote to sim: "+data+"\n")
    bytesToRead = sim.inWaiting()
    with open("/KWH/datalogger/transceive/simServer.log", "a") as log:
        log.write("bytes to read: "+str(bytesToRead)+"\n")
    resp = sim.read(bytesToRead)
    comslog = open("/KWH/datalogger/transceive/tcp/SIMComs.log", "a+")
    comslog.write(resp)
    comslog.close()
    cs.close()
