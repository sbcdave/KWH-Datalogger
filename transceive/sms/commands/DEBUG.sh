#!/bin/bash

# Command file for resetting the admin password

. /kwh/config.conf

log=/kwh/transceive/sms/commands/DEBUG.log

response="$STA - DEBUG value is now: $2"

/kwh/config/setConf.sh DEBUG $2
wait

echo "setconf DEBUG $2" > $log

/kwh/transceive/sms/smsSend.sh $1 $response
wait

echo "Response sent to $1: $response" >> $log

echo `date` >> $log
