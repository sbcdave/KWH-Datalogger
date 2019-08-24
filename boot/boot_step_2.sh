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
