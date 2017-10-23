#!/bin/bash

# use the "at" alias instead of this script to receive the SIM response
# via viewing the last 100 characters of the ttyAMA0.log
. /KWH/datalogger/transceive/ttyAMA0_setup.sh &&
sleep 1
echo "AT$*" > /dev/ttyAMA0
