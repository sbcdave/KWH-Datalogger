#!/usr/bin/env python
import signal
import minimalmodbus
import sys

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
    with open("/KWH/datalogger/modbus/queryAll.log", "a") as log:
	log.write(logText)

minimalmodbus.PARITY='E'
minimalmodbus.BAUDRATE=1200
minimalmodbus.STOPBITS=1
minimalmodbus.BYTESIZE=8
minimalmodbus.TIMEOUT=1
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL=True

mb=minimalmodbus.Instrument('/dev/ttyUSB0', int(sys.argv[1]), mode='rtu')

with open('/KWH/datalogger/modbus/values/m'+sys.argv[1]+'Voltage', 'w') as f:
    f.write(str(mb.read_float(0, 4, 2)))

with open('/KWH/datalogger/modbus/values/m'+sys.argv[1]+'Current', 'w') as f:
    f.write(str(mb.read_float(6, 4, 2)))

with open('/KWH/datalogger/modbus/values/m'+sys.argv[1]+'ActivePower', 'w') as f:
    f.write(str(mb.read_float(12, 4, 2)))

with open('/KWH/datalogger/modbus/values/m'+sys.argv[1]+'ApparentPower', 'w') as f:
    f.write(str(mb.read_float(18, 4, 2)))

with open('/KWH/datalogger/modbus/values/m'+sys.argv[1]+'ReactivePower', 'w') as f:
    f.write(str(mb.read_float(24, 4, 2)))

with open('/KWH/datalogger/modbus/values/m'+sys.argv[1]+'PowerFactor', 'w') as f:
    f.write(str(mb.read_float(30, 4, 2)))

with open('/KWH/datalogger/modbus/values/m'+sys.argv[1]+'PhaseAngle', 'w') as f:
    f.write(str(mb.read_float(36, 4, 2)))

with open('/KWH/datalogger/modbus/values/m'+sys.argv[1]+'Frequency', 'w') as f:
    f.write(str(mb.read_float(70, 4, 2)))

with open('/KWH/datalogger/modbus/values/m'+sys.argv[1]+'ImportActiveEnergy', 'w') as f:
    f.write(str(mb.read_float(72, 4, 2)))

with open('/KWH/datalogger/modbus/values/m'+sys.argv[1]+'ExportActiveEnergy', 'w') as f:
    f.write(str(mb.read_float(74, 4, 2)))

with open('/KWH/datalogger/modbus/values/m'+sys.argv[1]+'ImportReactiveEnergy', 'w') as f:
    f.write(str(mb.read_float(76, 4, 2)))

with open('/KWH/datalogger/modbus/values/m'+sys.argv[1]+'ExportReactiveEnergy', 'w') as f:
    f.write(str(mb.read_float(78, 4, 2)))

with open('/KWH/datalogger/modbus/values/m'+sys.argv[1]+'TotalActiveEnergy', 'w') as f:
    f.write(str(mb.read_float(342, 4, 2)))

with open('/KWH/datalogger/modbus/values/m'+sys.argv[1]+'TotalReactiveEnergy', 'w') as f:
    f.write(str(mb.read_float(344, 4, 2)))

