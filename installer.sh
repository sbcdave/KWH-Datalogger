#!/bin/bash

sudo apt-get install git
cd /
sudo git clone https://github.com/sbcdave/KWH.git
cd /usr/lib
sudo git clone https://github.com/joan2937/pigpio.git
cd /usr/lib/pigpio
make
sudo make install

sudo ln -n /KWH/datalogger/conf/datalogger.conf /etc/defaults/datalogger.conf
sudo printf "\n. /KWH/datalogger/conf/datalogger.conf\n" >> /etc/profile
sudo printf "\n. /KWH/datalogger/conf/datalogger.conf\n" >> /root/.bashrc
printf "\n. /KWH/datalogger/conf/datalogger.conf\n" >> /home/pi/.bashrc
source /KWH/datalogger/conf/datalogger.conf

sudo mv /KWH/datalogger/moves/dcrond /etc/cron.d/.
sudo chmod 644 /etc/cron.d/dcrond
