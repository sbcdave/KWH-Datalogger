#!/bin/bash

log=/KWH/transceive/sms/commands/inqConf.log
echo -n "" > $log
for conf in `cat /KWH/config/VARS`; do
    echo -n $msg$conf":"`cat /KWH/config/$conf`" " >> $log
done
wait

source /KWH/transceive/sms/smsSend.sh $1 `cat $log`
wait

echo "SMS to $1: $msg" >> $log

echo `date` >> $log
