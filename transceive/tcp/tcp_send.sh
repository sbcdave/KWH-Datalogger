#!/bin/bash

SIM_PORT=$(echo 'SELECT value FROM kwh.config WHERE `key` = "SIM_PORT" AND active = 1' | mysql -u pi); 
SIM_PORT=${SIM_PORT:6}
PORT=$(echo 'SELECT value FROM kwh.config WHERE `key` = "PORT" AND active = 1' | mysql -u pi); 
PORT=${PORT:6}
DOMAIN=$(echo 'SELECT value FROM kwh.config WHERE `key` = "DOMAIN" AND active = 1' | mysql -u pi); 
DOMAIN=${DOMAIN:6}
APN=$(echo 'SELECT value FROM kwh.config WHERE `key` = "APN" AND active = 1' | mysql -u pi); 
APN=${APN:6}

lock_file=/kwh/config/SIM_LOCK

. /kwh/config/kwh.conf

log="/kwh/log/tcp_send.log"
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

echo $1 | nc localhost $SIM_PORT >> $log
wait

echo AT+CIPCLOSE | nc localhost $SIM_PORT >> $log
wait
echo AT+CIPSHUT | nc localhost $SIM_PORT >> $log
wait

# Return lock
sudo rm -f $lock_file
wait
