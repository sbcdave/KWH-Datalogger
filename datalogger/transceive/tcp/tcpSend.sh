#!/bin/bash

lock_file=/KWH/datalogger/config/SIM_LOCK

. /KWH/datalogger/config/datalogger.conf

log="/KWH/datalogger/transceive/tcp/tcpSend.log"
wait

# Wait for lock
lockfile -1 -l 100 $lock_file
wait

# Send data to server
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
echo AT+CSTT=\"$APN\" | nc localhost $SIM_PORT >> $log
wait
echo AT+CIICR | nc localhost $SIM_PORT >> $log
wait
echo AT+CIFSR | nc localhost $SIM_PORT >> $log
wait
echo AT+CIPSTART=\"TCP\",\"$DOMAIN\",\"$PORT\" \
	| nc localhost $SIM_PORT >> $log
wait
echo AT+CIPSEND | nc localhost $SIM_PORT >> $log
wait
cat /KWH/datalogger/transceive/tcp/tstring \
	| nc localhost $SIM_PORT >> $log
wait
echo AT+CIPCLOSE | nc localhost $SIM_PORT >> $log
wait
echo AT+CIPSHUT | nc localhost $SIM_PORT >> $log
wait

# Return lock
sudo rm -f $lock_file
wait
