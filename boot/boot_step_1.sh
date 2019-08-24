#!/bin/bash
# First steps at boot, before starting, simserver.service
# ensure the SIM_LOCK is gone for propper sim lock accessibility,
# kill the scheduler by removing the scheduler file, and ensure the wifi
# module is disabled to save on power.

# This allows us to ensure a reliable boot sequence and to launch
# the simserver.service only after updating the time via sakis3g.

# The simserver.service is dependent on completion of these services
# and after simserver.service is started we re-enable the scheduler
# via kwh_start_TX.service, which is dependent on completion of
# simserver.service

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
sleep 5
wait
