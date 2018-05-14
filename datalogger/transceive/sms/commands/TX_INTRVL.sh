#!/bin/bash
# Command file for resetting the admin password

. /KWH/datalogger/config/datalogger.conf

log=/KWH/datalogger/transceive/sms/commands/TX_INTRVL.log

response="$STA - TX_INTRVL is now: $2"

/KWH/datalogger/config/setConf.sh TX_INTRVL $2
wait

echo "setconf TX_INTRVL $2" > $log

/KWH/datalogger/transceive/sms/smsSend.sh $1 $response
wait

echo "Response sent to $1: $response" >> $log

echo `date` >> $log
