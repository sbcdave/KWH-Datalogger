#!/bin/bash

############################
# Run code to collect data #
############################


# Truncate data table to remove old redundant data that is already
# in the tx_string table
echo "truncate datalogger.data" | mysql -u pi

# Start with timestamp to ensure all data points are linked in the 
# database via the minute they were collected
# Datetime stamp
/KWH/datalogger/datetime/datetime.py
wait
echo "datetime: $?" >> /KWH/datalogger/log/collect_data.log
dtm=`cat /KWH/datalogger/datetime/datetime`

# Analog inputs
/KWH/datalogger/data_collectors/analog.py $dtm
wait
echo "capture: $?" > /KWH/datalogger/log/collect_data.log

# Temp sensors
/KWH/datalogger/data_collectors/temp.sh $dtm
wait
echo "temp: $?" >> /KWH/datalogger/log/collect_data.log

# Signal Quality
/KWH/datalogger/data_collectors/signal.sh $dtm
wait
echo "signal: $?" >> /KWH/datalogger/log/collect_data.log

# ModBus
/KWH/datalogger/data_collectors/modbus.py $dtm
echo "modbus: $?" >> /KWH/datalogger/log/collect_data.log
wait

###################################
# Build transmitable ASCII string #
###################################

/KWH/datalogger/transceive/tcp/tx_string.py $dtm
# Decpricated by sakis3g
# echo $'\cZ' >> /KWH/datalogger/transceive/tcp/tstring
wait
echo "tx_string: $?" >> /KWH/datalogger/log/collect_data.log

#############################
# Initiate TCP transmission #
#############################

# Decpricated by sakis3g
#. /KWH/datalogger/transceive/tcp/tcpSend.sh >> \
#/KWH/datalogger/transceive/tcp/collect_data.log 2>&1
#wait
#echo "tcpSend: $?" >> /KWH/datalogger/transceive/tcp/collect_data.log

nc kwhstg.org 11001 < /KWH/datalogger/log/tstring

#########################################
# Check for new SMS messages to process #
#########################################

# Moved due to switching to sakis3g
#/KWH/datalogger/transceive/sms/smsParse.py >> /KWH/datalogger/transceive/sms/smsParse.log
#wait
#echo "smsParse: $?" >> /KWH/datalogger/transceive/tcp/collect_data.log

