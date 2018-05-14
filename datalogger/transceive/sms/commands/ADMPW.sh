#!/bin/bash
# Command file for resetting the admin password

. /KWH/datalogger/config/datalogger.conf

response="$STA - Admin password is now: $2"

/KWH/datalogger/config/setConf.sh ADMPW $2
wait

echo "setconf ADMPW $2" > /KWH/datalogger/transceive/sms/commands/ADMPW.log

/KWH/datalogger/transceive/sms/smsSend.sh $1 $response
wait

echo "Response sent to $1: $response" >> /KWH/datalogger/transceive/sms/commands/ADMPW.log

echo `date` >> /KWH/datalogger/transceive/sms/commands/ADMPW.log
