#!/bin/bash
# Command file for resetting the admin password

. /KWH/config.conf

log=/KWH/transceive/sms/commands/DOMAIN.log

response="$STA - DOMAIN is now: $2"

/KWH/config/setConf.sh DOMAIN $2
wait

echo "setconf DOMAIN $2" > $log

/KWH/transceive/sms/smsSend.sh $1 $response
wait

echo "Response sent to $1: $response" >> $log

echo `date` >> $log
