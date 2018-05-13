#!/bin/bash
msg=""
for conf in `cat /KWH/datalogger/config/VARS`; do
    msg="$msg$conf:"`cat /KWH/datalogger/config/$conf`";"
done
echo $msg > /KWH/datalogger/transceive/sms/commands/inqConf.log
