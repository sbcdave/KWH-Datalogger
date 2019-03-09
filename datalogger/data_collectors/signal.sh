#!/bin/bash

lock_file=/KWH/datalogger/config/SIM_LOCK

. /KWH/datalogger/config/datalogger.conf

lockfile -1 -l 100 $lock_file
wait

echo AT+CSQ | nc localhost $SIM_PORT > /KWH/datalogger/log/signal.log
wait
sq=$(grep '\+CSQ:' /KWH/datalogger/log/signal.log | sed -E 's/\+CSQ: ([0-9]*),.*/\1/')
wait
sql="INSERT INTO datalogger.data VALUES (\"$@\",\"SQ\",$sq)"
echo $sql | mysql -u pi

sudo rm -f $lock_file
wait
