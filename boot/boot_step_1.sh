#!/bin/bash
# First steps at boot, before starting, simserver.service
# ensure the SIM_LOCK is gone for propper sim lock accessibility,
# kill the scheduler by removing the scheduler file, and ensure the wifi
# module is disabled to save on power.

# This allows us to ensure a reliable boot sequence and to launch
# the sim_server.py only after updating the time via sakis3g.

# Only after sim_server.py is started we re-enable the scheduler

# lock cleanup
sudo rm /kwh/config/SIM_LOCK
wait

# stop kwh scheduler
sudo rm /etc/cron.d/kwh_scheduler.cron
wait

# shutdown wifi module
sudo ifconfig wlan0 down
wait

# sleep to ensure all needed service are up before starting up sakis3g
# in the next step
sleep 10
wait

# start internet connection via sakis3g
sudo /kwh/lib/sakis3g/sakis3g connect --console
wait

# use three step ntp process to set time via RPi time service
sudo /etc/init.d/ntp stop
wait

sudo ntpd -q -g
wait

sudo /etc/init.d/ntp start
wait

# shut off sakis3g connection
sudo /kwh/lib/sakis3g/sakis3g disconnect --console
wait

# start sim_server.py
sudo /kwh/transceive/sim_server.py &
wait

# re-implement the scheduler
sudo cp /kwh/boot/kwh_scheduler.cron /etc/cron.d/kwh_scheduler.cron
