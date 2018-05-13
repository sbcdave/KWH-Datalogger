#!/bin/bash

/KWH/datalogger/config/setConf.sh STA $1 
echo "setconf STA $1" > /KWH/datalogger/transceive/sms/commands/STA.log
