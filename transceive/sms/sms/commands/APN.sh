#!/bin/bash

# Command file for resetting the admin password

. /kwh/config.conf

log=/kwh/transceive/sms/commands/APN.log

response="$STA - APN is now: $2"

/kwh/config/setConf.sh APN $2
echo "setconf APN $2" > $log
wait

/kwh/transceive/sms/smsSend.sh $1 $response
wait

echo "Response sent to $1: $response" >> $log

echo `date` >> $log
