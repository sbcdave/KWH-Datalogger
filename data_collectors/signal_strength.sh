#!/bin/bash

lock_file=/kwh/config/SIM_LOCK

. /kwh/config/kwh.conf

lockfile -1 -l 100 $lock_file
wait

echo AT+CSQ | nc localhost $SIM_PORT > /kwh/log/signal_strength.log
wait
sq=$(grep '\+CSQ:' /kwh/log/signal_strength.log | sed -E 's/\+CSQ: ([0-9]*),.*/\1/')
wait
sql="INSERT INTO kwh.data VALUES (\"$@\",\"SQ\",$sq)"
echo $sql | mysql -u pi

sudo rm -f $lock_file
wait
