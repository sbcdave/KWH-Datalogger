#!/bin/bash

# Command file for resetting the admin password

. /KWH/datalogger/config/datalogger.conf

log=/KWH/datalogger/transceive/sms/commands/ADxx.log

if [ "$3" == "1" ]; then
    response="$STA - Analog Channel $2: enabled"
else
    response="$STA - Analog Channel $2: disabled"
fi

/KWH/datalogger/config/setConf.sh AD$2 $3
wait

echo "setconf AD$2 $3" > $log

/KWH/datalogger/transceive/sms/smsSend.sh $1 $response
wait

echo "Response sent to $1: $response" >> $log

echo `date` >> $log
