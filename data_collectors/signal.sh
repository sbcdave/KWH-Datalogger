#!/bin/bash

lock_file=/KWH/config/SIM_LOCK

. /KWH/config.conf

lockfile -1 -l 100 $lock_file
wait

echo AT+CSQ | nc localhost $SIM_PORT > /KWH/log/signal.log
wait
sq=$(grep '\+CSQ:' /KWH/log/signal.log | sed -E 's/\+CSQ: ([0-9]*),.*/\1/')
wait
sql="INSERT INTO datalogger.data VALUES (\"$@\",\"SQ\",$sq)"
echo $sql | mysql -u pi

sudo rm -f $lock_file
wait
