#!/bin/bash

lock_file=/kwh/config/SIM_LOCK

. /kwh/config.conf

log="/kwh/datetime/datetime.log"
wait

lockfile -1 -l 120 $lock_file
wait

echo AT+CMEE=2 | nc localhost $SIM_PORT > $log
wait
echo AT+CIPSHUT | nc localhost $SIM_PORT >> $log
wait
echo AT+CGATT=0 | nc localhost $SIM_PORT >> $log
wait
echo AT+CGATT=1 | nc localhost $SIM_PORT >> $log
wait
echo AT+CIPSHUT | nc localhost $SIM_PORT >> $log
wait
echo AT+CIPMUX=0 | nc localhost $SIM_PORT >> $log
wait
echo AT+CSTT=\"wholesale\" | nc localhost $SIM_PORT >> $log
wait
echo AT+CIICR | nc localhost $SIM_PORT >> $log
wait
echo AT+CIFSR | nc localhost $SIM_PORT >> $log
wait
echo AT+CIPSTART=\"TCP\",\"time.nist.gov\",\"37\" \
	| nc localhost $SIM_PORT | tail -c 4 > /kwh/datetime/nisttime
wait
echo AT+CIPCLOSE | nc localhost $SIM_PORT >> $log
wait
echo AT+CIPSHUT | nc localhost $SIM_PORT >> $log
wait
/kwh/datetime/setTime.sh $(tail -c 4 /kwh/datetime/nisttime)
wait

sudo rm -f $lock_file
wait
