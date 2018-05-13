#!/bin/bash

/KWH/datalogger/config/setConf.sh AD$1 $2 
echo "setconf AD$1 $2" > /KWH/datalogger/transceive/sms/commands/ADxx.log
