#!/bin/bash

/KWH/datalogger/config/setConf.sh DEBUG $1 
echo "setconf DEBUG $1" > /KWH/datalogger/transceive/sms/commands/DEBUG.log
