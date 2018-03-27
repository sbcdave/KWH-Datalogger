#!/bin/bash
if [ ! -z $1 ] && [ ! -z $2 ] && [ -z $4 ]; then
    if [ ! -f /KWH/datalogger/config/$1 ]; then
        fileExists=true
    fi
    echo -n $2 > /KWH/datalogger/config/$1 &&
    export $1=$2 &&
    if [ "$fileExists" = "true" ]; then
        echo "export $1=\`cat /KWH/datalogger/config/$1\`" \
	>> /KWH/datalogger/config/vars &&
        printf "with open('/KWH/datalogger/config/$1') as config:\n\t$1=config.read()\n" \
	>> /KWH/datalogger/config/pyvars.py &&
        echo $1 >> /KWH/datalogger/config/VARS
	fileExists=false
    fi
else
    echo "Usage: setconf <variable-name> <value> <optional: path>"
fi
