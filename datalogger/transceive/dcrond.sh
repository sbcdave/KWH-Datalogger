#!/bin/bash

# This is called by cron every minute to transmit the
# data that the data logger has collected/(is currently sensing)

sudo flock -x /KWH/datalogger/conf/SIM_LOCK /KWH/datalogger/transceive/tcp/transmit.sh
sleep 1 &&
sudo killall cat
