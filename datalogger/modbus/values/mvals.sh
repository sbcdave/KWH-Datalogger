#!/bin/bash
for file in `ls /KWH/datalogger/modbus/values`; do
    if [ ! "$file" == "mvals.sh" ]; then
        echo -n $file' ';
        cat /KWH/datalogger/modbus/values/$file;
        echo '';
    fi
done
