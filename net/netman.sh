#!/bin/bash
# Load alias so setconf will work
source /kwh/config/kwh.conf

# This will run all tx methods we have created with APN wholesale
setconf APN wholesale
sudo cp /kwh/net/APNs/wholesale.conf /etc/sakis3g.conf
wait
/kwh/net/net.sh
wait

# APN airtel
setconf APN airtel
sudo cp /kwh/net/APNs/airtel.conf /etc/sakis3g.conf
wait
/kwh/net/net.sh
wait

# APN internet without specifying username and password
setconf APN internet
sudo cp /kwh/net/APNs/internetNoUserPass.conf /etc/sakis3g.conf
wait
/kwh/net/net.sh
wait

# APN internet specifying username and password
setconf APN internet
sudo cp /kwh/net/APNs/internetWithUserPass.conf /etc/sakis3g.conf
wait
/kwh/net/net.sh
wait

# APN mtn without specifying username and password
setconf APN mtn
sudo cp /kwh/net/APNs/mtnNoUserPass.conf /etc/sakis3g.conf
wait
/kwh/net/net.sh
wait

# APN mtn specifying username and password
setconf APN mtn
sudo cp /kwh/net/APNs/mtnWithUserPass.conf /etc/sakis3g.conf
wait
/kwh/net/net.sh
wait

