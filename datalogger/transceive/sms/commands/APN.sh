#!/bin/bash

# Command file for resetting the admin password

. /KWH/datalogger/config/datalogger.conf

log=/KWH/datalogger/transceive/sms/commands/APN.log

response="$STA - APN is now: $2"

/KWH/datalogger/config/setConf.sh APN $2
echo "setconf APN $2" > $log
wait

/KWH/datalogger/transceive/sms/smsSend.sh $1 $response
wait

echo "Response sent to $1: $response" >> $log

echo `date` >> $log
