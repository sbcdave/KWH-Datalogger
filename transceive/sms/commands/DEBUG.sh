#!/bin/bash

# Command file for resetting the admin password

. /KWH/config.conf

log=/KWH/transceive/sms/commands/DEBUG.log

response="$STA - DEBUG value is now: $2"

/KWH/config/setConf.sh DEBUG $2
wait

echo "setconf DEBUG $2" > $log

/KWH/transceive/sms/smsSend.sh $1 $response
wait

echo "Response sent to $1: $response" >> $log

echo `date` >> $log
