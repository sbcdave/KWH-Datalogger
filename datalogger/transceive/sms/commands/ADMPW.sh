#!/bin/bash

/KWH/datalogger/config/setConf.sh ADMPW $1 
echo "setconf ADMPW $1" > /KWH/datalogger/transceive/sms/commands/ADMPW.log
