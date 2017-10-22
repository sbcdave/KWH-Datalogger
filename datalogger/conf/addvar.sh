#!/bin/bash
if [ ! -z $1 ] && [ ! -z $2 ] && [ -z $4 ]; then
    if [ ! -f $1 ]; then
        fileExists=true
    fi
    echo -n $2 > /KWH/datalogger/conf/$1 &&
    export $1=$2 &&
    if [ "$fileExists" = "true" ]; then
        echo "export $1=\`cat /KWH/datalogger/conf/$1\`" \
>> /KWH/datalogger/conf/vars &&
        printf "with open('/KWH/datalogger/conf/$1') as conf:\n\t$1=conf.read()\n" \
>> /KWH/datalogger/conf/pyvars.py &&
        echo $1 >> /KWH/datalogger/conf/VARS
	fileExists=false
    fi
else
    echo "Usage: addvar <variable-name> <value> <optional: path>"
fi
