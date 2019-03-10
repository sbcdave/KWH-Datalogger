#!/bin/bash

log=/kwh/transceive/sms/commands/inqConf.log
echo -n "" > $log
for conf in `cat /kwh/config/VARS`; do
    echo -n $msg$conf":"`cat /kwh/config/$conf`" " >> $log
done
wait

source /kwh/transceive/sms/smsSend.sh $1 `cat $log`
wait

echo "SMS to $1: $msg" >> $log

echo `date` >> $log
