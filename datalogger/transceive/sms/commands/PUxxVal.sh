#!/bin/bash
# Command file for resetting the admin password

. /KWH/datalogger/config/datalogger.conf

log=/KWH/datalogger/transceive/sms/commands/PUxxVal.log

response="$STA - PU$2 value is now: $3"

path="/KWH/datalogger/pulse/PU"$2
echo -n "$3" > $path
echo "$3 > $path" > $log

/KWH/datalogger/transceive/sms/smsSend.sh $1 $response
wait

echo "Response sent to $1: $response" >> $log

echo `date` >> $log
