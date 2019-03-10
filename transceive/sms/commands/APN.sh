#!/bin/bash

# Command file for resetting the admin password

. /KWH/config.conf

log=/KWH/transceive/sms/commands/APN.log

response="$STA - APN is now: $2"

/KWH/config/setConf.sh APN $2
echo "setconf APN $2" > $log
wait

/KWH/transceive/sms/smsSend.sh $1 $response
wait

echo "Response sent to $1: $response" >> $log

echo `date` >> $log
