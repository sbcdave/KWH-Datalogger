#!/bin/bash

lock_file=/kwh/config/SIM_LOCK

. /kwh/config.conf

wait

lockfile -1 -l 100 $lock_file
wait

echo AT+CMGF=1 | nc localhost $SIM_PORT \
	> /kwh/transceive/sms/delete.txt
wait
echo AT+CMGD=1,4 | nc localhost $SIM_PORT \
	>> /kwh/transceive/sms/delete.txt
wait

sudo rm -f $lock_file
wait
