#!/bin/bash
# Command file for resetting the admin password

. /KWH/datalogger/config/datalogger.conf

log=/KWH/datalogger/transceive/sms/commands/PUxx.log 

response="$STA - PU$2 is now: $3"

/KWH/datalogger/config/setConf.sh PU$2 $3

echo "setconf PU$2 $3" > $log

/KWH/datalogger/transceive/sms/smsSend.sh $1 $response
wait

echo "Response sent to $1: $response" >> $log

echo `date` >> $log
