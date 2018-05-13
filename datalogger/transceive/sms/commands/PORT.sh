#!/bin/bash

/KWH/datalogger/config/setConf.sh PORT $1 
echo "setconf PORT $1" > /KWH/datalogger/transceive/sms/commands/PORT.log
