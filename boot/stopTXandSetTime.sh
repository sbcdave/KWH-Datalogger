#!/bin/bash
sudo rm /kwh/config/SIM_LOCK
wait
sudo rm /etc/cron.d/dcrond
wait
sleep 10
wait
/kwh/datetime/getTime.sh
wait
sudo cp /kwh/moves/dcrond /etc/cron.d/dcrond
