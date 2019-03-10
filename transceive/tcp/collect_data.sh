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
/KWH/datetime/datetime.py
wait
echo "datetime: $?" >> /KWH/log/collect_data.log
dtm=`cat /KWH/datetime/datetime`

# Analog inputs
/KWH/data_collectors/analog.py $dtm
wait
echo "capture: $?" > /KWH/log/collect_data.log

# Temp sensors
/KWH/data_collectors/temp.sh $dtm
wait
echo "temp: $?" >> /KWH/log/collect_data.log

# Signal Quality
/KWH/data_collectors/signal.sh $dtm
wait
echo "signal: $?" >> /KWH/log/collect_data.log

# ModBus
/KWH/data_collectors/modbus.py $dtm
echo "modbus: $?" >> /KWH/log/collect_data.log
wait

###################################
# Build transmitable ASCII string #
###################################

/KWH/transceive/tcp/tx_string.py $dtm
# Decpricated by sakis3g
# echo $'\cZ' >> /KWH/transceive/tcp/tstring
wait
echo "tx_string: $?" >> /KWH/log/collect_data.log

#############################
# Initiate TCP transmission #
#############################

# Decpricated by sakis3g
#. /KWH/transceive/tcp/tcpSend.sh >> \
#/KWH/transceive/tcp/collect_data.log 2>&1
#wait
#echo "tcpSend: $?" >> /KWH/transceive/tcp/collect_data.log

nc kwhstg.org 11001 < /KWH/transceive/tcp/tstring

#########################################
# Check for new SMS messages to process #
#########################################

# Moved due to switching to sakis3g
#/KWH/transceive/sms/smsParse.py >> /KWH/transceive/sms/smsParse.log
#wait
#echo "smsParse: $?" >> /KWH/transceive/tcp/collect_data.log

