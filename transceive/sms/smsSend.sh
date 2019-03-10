#!/bin/bash

lock_file=/kwh/config/SIM_LOCK

# Explain usage
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: sendsms <phone number> <message>";
    exit 0;
fi

. /kwh/config.conf

log="/kwh/transceive/sms/smsSend.log"
wait

# Wait for lock
lockfile -1 -l 100 $lock_file
wait

# Prep SIM800 for SMS
echo AT+CMGF=1 | nc localhost $SIM_PORT > $log
wait

# Start message to input phone number
echo AT+CMGS=\"$1\" | nc localhost $SIM_PORT >> $log
wait

# Input message
echo -n ${@: -`expr $# - 1`} | nc localhost $SIM_PORT >> $log
wait

# Send message
echo $'\cZ' | nc localhost $SIM_PORT >> $log
wait

# Return lock
sudo rm -f $lock_file
wait
