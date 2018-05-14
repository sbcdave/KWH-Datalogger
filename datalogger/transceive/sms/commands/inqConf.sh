#!/bin/bash

log=/KWH/datalogger/transceive/sms/commands/inqConf.log
echo -n "" > $log
for conf in `cat /KWH/datalogger/config/VARS`; do
    echo -n $msg$conf":"`cat /KWH/datalogger/config/$conf`" " >> $log
done
wait

source /KWH/datalogger/transceive/sms/smsSend.sh $1 `cat $log`
wait

echo "SMS to $1: $msg" >> $log

echo `date` >> $log
