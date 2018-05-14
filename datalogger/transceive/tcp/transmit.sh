#!/bin/bash

############################
# Run code to collect data #
############################

# Analog inputs
/KWH/datalogger/adc/capture.py
wait
echo "capture: $?" > /KWH/datalogger/transceive/tcp/transmit.log

# Datetime stamp
/KWH/datalogger/datetime/datetime.py
wait
echo "datetime: $?" >> /KWH/datalogger/transceive/tcp/transmit.log

# Temp sensors
/KWH/datalogger/temperature/temp.sh
wait
echo "temp: $?" >> /KWH/datalogger/transceive/tcp/transmit.log

#/KWH/datalogger/modbus/modbus....
#echo "modbus: $?" >> /KWH/datalogger/transceive/tcp/transmit.log
#wait
# Signal Quality
/KWH/datalogger/signal/getSignal.sh
wait
echo "signal: $?" >> /KWH/datalogger/transceive/tcp/transmit.log

###################################
# Build transmitable ASCII string #
###################################

/KWH/datalogger/transceive/tcp/tstring.py
echo $'\cZ' >> /KWH/datalogger/transceive/tcp/tstring
wait
echo "tstring: $?" >> /KWH/datalogger/transceive/tcp/transmit.log

#############################
# Initiate TCP transmission #
#############################

. /KWH/datalogger/transceive/tcp/tcpSend.sh >> \
/KWH/datalogger/transceive/tcp/transmit.log 2>&1
wait
echo "tcpSend: $?" >> /KWH/datalogger/transceive/tcp/transmit.log

#########################################
# Check for new SMS messages to process #
#########################################

/KWH/datalogger/transceive/sms/smsParse.py > /KWH/datalogger/transceive/sms/smsParse.log
wait
echo "smsParse: $?" >> /KWH/datalogger/transceive/tcp/transmit.log
