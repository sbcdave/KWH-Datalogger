#!/bin/bash

# Command file for resetting the admin password

. /kwh/config.conf

log=/kwh/transceive/sms/commands/APN.log

response="$STA - APN is now: $2"

/kwh/config/set_apn.py $2
echo "setapn $2" > $log
wait

/kwh/transceive/sms/smsSend.sh $1 $response
wait

echo "Response sent to $1: $response" >> $log

echo `date` >> $log
