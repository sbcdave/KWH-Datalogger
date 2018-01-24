#!/bin/bash

############################
# Run code to collect data #
############################

# Analog inputs
/KWH/datalogger/adc/capture.py
echo "capture: $?" > /KWH/datalogger/transceive/tcp/transmit.log

# Datetime stamp
/KWH/datalogger/datetime/datetime.py
echo "datetime: $?" >> /KWH/datalogger/transceive/tcp/transmit.log

# Temp sensors
/KWH/datalogger/temp/temp.sh
echo "temp: $?" >> /KWH/datalogger/transceive/tcp/transmit.log

#/KWH/datalogger/modbus/modbus....
#echo "modbus: $?" >> /KWH/datalogger/transceive/tcp/transmit.log

###################################
# Build transmitable ASCII string #
###################################

/KWH/datalogger/transceive/tcp/tstring.py
echo $'\cZ' >> /KWH/datalogger/transceive/tcp/tstring
echo "tstring: $?" >> /KWH/datalogger/transceive/tcp/transmit.log

#############################
# Initiate TCP transmission #
#############################

. /KWH/datalogger/transceive/tcp/tcpSend.sh >> \
/KWH/datalogger/transceive/tcp/transmit.log 2>&1
echo "tcpSend: $?" >> /KWH/datalogger/transceive/tcp/transmit.log
