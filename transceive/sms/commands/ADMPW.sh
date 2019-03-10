#!/bin/bash
# Command file for resetting the admin password

. /KWH/config.conf

response="$STA - Admin password is now: $2"

/KWH/config/setConf.sh ADMPW $2
wait

echo "setconf ADMPW $2" > /KWH/transceive/sms/commands/ADMPW.log

/KWH/transceive/sms/smsSend.sh $1 $response
wait

echo "Response sent to $1: $response" >> /KWH/transceive/sms/commands/ADMPW.log

echo `date` >> /KWH/transceive/sms/commands/ADMPW.log
