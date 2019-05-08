#!/bin/bash

############################
# Run code to collect data #
############################


# Truncate data table to remove old redundant data that is already
# in the tx_string table
echo "truncate kwh.data" | mysql -u pi

# Start with timestamp to ensure all data points are linked in the 
# database via the minute they were collected
# Datetime stamp
dtm=`date +%s`
wait
echo "datetime: $?" >> /kwh/log/collect_data.log
echo "datetime: $?"

# RPi Processor Temp
/kwh/data_collectors/rpi_temp.sh $dtm
wait
echo "rpi temp: $?" >> /kwh/log/collect_data.log
echo "rpi temp: $?"

# RPi Disk Use
/kwh/data_collectors/disk_space.sh $dtm
wait
echo "rpi disk: $?" >> /kwh/log/collect_data.log
echo "rpi disk: $?"

# Signal Quality
/kwh/data_collectors/signal_strength.sh $dtm
wait
echo "signal: $?" >> /kwh/log/collect_data.log
echo "signal: $?"

###################################
# Build transmitable ASCII string #
###################################

/kwh/transceive/tcp/tx_string.py $dtm
# Decpricated by sakis3g
# echo $'\cZ' >> /kwh/transceive/tcp/tstring
wait
echo "tx_string: $?" >> /kwh/log/collect_data.log
echo "tx_string: $?"
