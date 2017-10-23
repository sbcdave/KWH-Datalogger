#!/bin/bash

sudo apt-get install git
cd /
sudo mkdir KWH
sudo chown -R pi:pi KWH
cd KWH
sudo git clone https://github.com/sbcdave/KWH.git

sudo ln -n /KWH/datalogger/conf/datalogger.conf /etc/defaults/datalogger.conf
sudo printf "\n. /KWH/datalogger/conf/datalogger.conf\n" >> /etc/profile
sudo printf "\n. /KWH/datalogger/conf/datalogger.conf\n" >> /root/.bashrc
printf "\n. /KWH/datalogger/conf/datalogger.conf\n" >> /home/pi/.bashrc
source /KWH/datalogger/conf/datalogger.conf

sudo mv /KWH/datalogger/moves/dcrond /etc/cron.d/.
sudo chmod 644 /etc/cron.d/dcrond
