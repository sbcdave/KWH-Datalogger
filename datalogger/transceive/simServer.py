#!/usr/bin/env python
import socket
import time
import signal
import sys
import serial
import os
import subprocess
# Load environment variables
execfile("/KWH/datalogger/conf/pyvars.py")

def signal_handler(signal, frame):
    if DEBUG == "1":
	log.write('Closing SIM Server\n')
       	log.close()
        comslog.close()
    sim.close()
    s.close()
    cs.close()
    exit(0)
signal.signal(signal.SIGINT, signal_handler)

if DEBUG == "1":
    log = open("/KWH/datalogger/transceive/simServer.log", "a")
    log.write("Starting SIM Server\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 9999
port_chosen = False

if DEBUG == "1":
    log.write("Starting port selection\n")

while not port_chosen:
    try:
	s.bind((host, port))
        port_chosen = True
    except:
	if DEBUG == "1":
            log.write("Port "+str(port)+" in use\n")
	port = port + 1

if DEBUG == "1":	
    log.write("Port "+str(port)+" selected\n")

with open("/KWH/datalogger/conf/SIM_PORT", "w") as SIM_PORT:
    SIM_PORT.write(str(port))

if DEBUG == "1":
    log.write("SIM_PORT: "+os.environ["SIM_PORT"]+"\n")
    log.write("Listening...\n")
    log.close()

s.listen(100)
sim = serial.Serial('/dev/ttyAMA0', 115200, timeout=5)
sim.flushInput()
sim.flushOutput()

while True:
    cs,addr = s.accept()
    subprocess.Popen("/KWH/datalogger/transceive/ttyAMA0_setup.sh")
    if DEBUG == "1":
	with open("/KWH/datalogger/transceive/simServer.log", "a") as log:
	    log.write("ttyAMA0_setup.sh complete!\n")    
    if DEBUG == "1":
	with open("/KWH/datalogger/transceive/simServer.log", "a") as log:
	    log.write("Accepted: "+str(addr)+"\n")
    data = cs.recv(1024)
    if DEBUG == "1":
	with open("/KWH/datalogger/transceive/simServer.log", "a") as log:
            log.write("Received: "+data+"\n")
    sim.write(data)
    if DEBUG == "1":
        with open("/KWH/datalogger/transceive/simServer.log", "a") as log:
            log.write("Wrote to sim: "+data+"\n")
    bytesToRead = sim.inWaiting()
    if bytesToRead < 1:
        if DEBUG == "1":
            with open("/KWH/datalogger/transceive/simServer.log", "a") as log:
                log.write("No SIM response...rebooting SIM!\n")
	execfile("/KWH/datalogger/transceive/reset_sim.py")
        if DEBUG == "1":
            with open("/KWH/datalogger/transceive/simServer.log", "a") as log:
                log.write("Sleeping 1 for SIM reboot!\n")
	time.sleep(1)
        if DEBUG == "1":
            with open("/KWH/datalogger/transceive/simServer.log", "a") as log:
                log.write("Configuring stty settings for SIM coms\n")
	subprocess.Popen("/KWH/datalogger/transceive/ttyAMA0_setup.sh")
	time.sleep(1)
    if DEBUG == "1":
        with open("/KWH/datalogger/transceive/simServer.log", "a") as log:
            log.write("Bytes to read: "+str(bytesToRead)+"\n")
    resp = sim.read(bytesToRead)
    if DEBUG == "1":
        with open("/KWH/datalogger/transceive/simServer.log", "a") as log:
            log.write("Sim response: "+resp+"\n")
    cs.send(resp)
    if DEBUG == "1":
        with open("/KWH/datalogger/transceive/simServer.log", "a") as log:
            log.write("Response sent to: "+str(addr)+"\n")
    cs.close()
