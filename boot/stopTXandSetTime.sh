#!/bin/bash
sudo rm /KWH/config/SIM_LOCK
wait
sudo rm /etc/cron.d/dcrond
wait
sleep 10
wait
/KWH/datetime/getTime.sh
wait
sudo cp /KWH/moves/dcrond /etc/cron.d/dcrond
