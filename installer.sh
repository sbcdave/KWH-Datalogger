#!/bin/bash

sudo apt-get install git
cd /
sudo mkdir KWH
sudo chown -R pi:pi KWH
cd KWH
sudo git clone https://github.com/sbcdave/KWH.git

#investigate shutting down uneccesary services

sudo ln -n /KWH/datalogger/conf/datalogger.conf /etc/defaults/datalogger.conf
sudo printf "\n. /KWH/datalogger/conf/datalogger.conf\n" >> /etc/profile
sudo printf "\n. /KWH/datalogger/conf/datalogger.conf\n" >> /root/.bashrc
printf "\n. /KWH/datalogger/conf/datalogger.conf\n" >> /home/pi/.bashrc
source /KWH/datalogger/conf/datalogger.conf

sudo mv /KWH/datalogger/moves/dcrond /etc/cron.d/.
sudo chmod 644 /etc/cron.d/dcrond

#add stuff here to setup config.txt for adding the dtoverlays for shutting
#off bluetooth
sudo systemctl mask serial-getty@ttyAMA0.service
