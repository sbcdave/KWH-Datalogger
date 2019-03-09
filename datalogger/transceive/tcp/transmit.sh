#!/bin/bash

############################
# Run code to collect data #
############################

# Start with timestamp to ensure all data points are linked in the 
# database via the minute they were collected

# Datetime stamp
/KWH/datalogger/datetime/datetime.py
wait
echo "datetime: $?" >> /KWH/datalogger/transceive/tcp/transmit.log

# Analog inputs
/KWH/datalogger/adc/capture.py
wait
echo "capture: $?" > /KWH/datalogger/transceive/tcp/transmit.log

# Temp sensors
/KWH/datalogger/temperature/temp.sh
wait
echo "temp: $?" >> /KWH/datalogger/transceive/tcp/transmit.log

# Signal Quality
/KWH/datalogger/signal/getSignal.sh
wait
echo "signal: $?" >> /KWH/datalogger/transceive/tcp/transmit.log

# ModBus
/KWH/datalogger/modbus/queryAll.py 1
echo "modbus: $?" >> /KWH/datalogger/transceive/tcp/transmit.log
wait

###################################
# Build transmitable ASCII string #
###################################

/KWH/datalogger/transceive/tcp/tstring.py
# Decpricated by sakis3g
# echo $'\cZ' >> /KWH/datalogger/transceive/tcp/tstring
wait
echo "tstring: $?" >> /KWH/datalogger/transceive/tcp/transmit.log

#############################
# Initiate TCP transmission #
#############################

# Decpricated by sakis3g
#. /KWH/datalogger/transceive/tcp/tcpSend.sh >> \
#/KWH/datalogger/transceive/tcp/transmit.log 2>&1
#wait
#echo "tcpSend: $?" >> /KWH/datalogger/transceive/tcp/transmit.log

nc kwhstg.org 11001 < /KWH/datalogger/transceive/tcp/tstring

#########################################
# Check for new SMS messages to process #
#########################################

# Moved due to switching to sakis3g
#/KWH/datalogger/transceive/sms/smsParse.py >> /KWH/datalogger/transceive/sms/smsParse.log
#wait
#echo "smsParse: $?" >> /KWH/datalogger/transceive/tcp/transmit.log

