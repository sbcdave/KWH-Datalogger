#!/bin/bash
sudo rm /KWH/datalogger/config/SIM_LOCK
wait
sudo rm /etc/cron.d/dcrond
wait
sleep 10
wait
/KWH/datalogger/datetime/getTime.sh
wait
sudo cp /KWH/moves/dcrond /etc/cron.d/dcrond
