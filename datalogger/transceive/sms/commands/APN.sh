#!/bin/bash

/KWH/datalogger/config/setConf.sh APN $1 
echo "setconf APN $1" > /KWH/datalogger/transceive/sms/commands/APN.log
