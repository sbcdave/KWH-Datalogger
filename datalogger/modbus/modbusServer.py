#!/usr/bin/env python
import socket
import time
import signal
from pymodbus.client.sync import ModbusSerialClient as msc
import subprocess

# Load environment variables
execfile("/KWH/datalogger/config/pyvars.py")
DEBUG = int(DEBUG)

def signal_handler(signal, frame):
    if DEBUG > 0: log('SIGINT received...Closing ModBus Server\n')
    ModBus.close()
    s.close()
    cs.close()
    exit(0)
signal.signal(signal.SIGINT, signal_handler)

# Log function
def log(logText):
    with open("/KWH/datalogger/modbus/modbusServer.log", "a") as log:
	log.write(logText)

if DEBUG > 0: log("Starting ModBus Server\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 19999
port_chosen = False

if DEBUG > 0: log("Starting port selection\n") 

# Find an open port for the service
while not port_chosen:
    try:
	s.bind((host, port))
        port_chosen = True
    except:
	if DEBUG > 0: log("Port "+str(port)+" in use\n")
	port = port + 1

# Update the env variables with the chosen active MODBUS_PORT
with open("/KWH/datalogger/config/MODBUS_PORT", "w") as MODBUS_PORT:
    MODBUS_PORT.write(str(port))

if DEBUG: log("MODBUS_PORT: "+str(port)+"\n")

execfile("/KWH/datalogger/config/pyvars.py")
DEBUG = int(DEBUG)
if DEBUG > 1: log("Configuration variables reloaded\n")    

if DEBUG: log("Listening...\n")

ModBus = msc(method='rtu',port='/dev/ttyUSB0', timeout=1, stopbits=1, \
bytesize=8, parity='E', baudrate = 1200)

if ModBus.connect():
    log("Connected\n")
else:
    log("Unable to connect\n")

s.listen(1)

# Daemon listen on MODBUS_PORT for ModBus commands
while True:
    # Waits for a command
    cs,addr = s.accept()

    # Configure block
    execfile("/KWH/datalogger/config/pyvars.py")
    DEBUG = int(DEBUG)
    if DEBUG: log("Configuration variables reloaded\n")    

    # Beginning to process received command
    cmd = cs.recv(1024)
    if DEBUG: log("Received: "+cmd+"\n")

    cmd = cmd.split(' ')
    # Send command to MODBUS
    try:
	r=ModBus.read_input_registers(address=int(cmd[0]),count=int(cmd[1])\
                                      ,unit=int(cmd[2]))

        if DEBUG: log("Requested "+cmd[1]+" registers, starting at " \
                      +"address "+cmd[0]+", from slave "+cmd[2])

        data = str(r.registers[0])+" "+str(r.registers[1])

        if DEBUG: log("Reponse: "+data+"\n")

        cs.send(data)
        if DEBUG: log("Response sent to: "+str(addr)+"\n")

    except Exception as e:
        log(str(e))
	execfile("/KWH/datalogger/config/pyvars.py")
        DEBUG = int(DEBUG)
	if DEBUG: log("\nConfiguration variables reloaded\n")    
        subprocess.Popen("/KWH/datalogger/transceive/ttyAMA0_setup.sh")

    cs.close()
    if DEBUG: log("Client connection closed\n")

ModBus.close()
