#!/bin/bash

lock_file=/KWH/datalogger/config/SIM_LOCK

. /KWH/datalogger/config/datalogger.conf

lockfile -1 -l 100 $lock_file
wait

echo AT+CSQ | nc localhost $SIM_PORT > /KWH/datalogger/signal/signal.log
wait
echo -n $(grep '\+CSQ:' /KWH/datalogger/signal/signal.log | sed -E 's/\+CSQ: ([0-9]*),.*/\1/') > /KWH/datalogger/signal/signal
wait

sudo rm -f $lock_file
wait
