#!/bin/bash

# Install git for pulling the code from the repository
sudo apt-get install git

# Install inotify for monitoring folders for:
#   Temp sensors
sudo apt-get install inotify-tools

# Move to root and download data logger code from github
cd /
sudo git clone https://github.com/sbcdave/KWH.git

# Change data logger code root directory owner:group to pi
sudo chown -R pi:pi KWH


#investigate shutting down uneccesary services

# Create symlink from /etc/defaults to datalogger.conf file
sudo ln -n /KWH/datalogger/config/datalogger.conf /etc/defaults/datalogger.conf
# Add datalogger.conf file to /etc/profile and to root and pi's .bashrc
sudo printf "\n. /KWH/datalogger/config/datalogger.conf\n" >> /etc/profile
sudo printf "\n. /KWH/datalogger/config/datalogger.conf\n" >> /root/.bashrc
printf "\n. /KWH/datalogger/config/datalogger.conf\n" >> /home/pi/.bashrc

# Source the datalogger.conf file into environment variables
source /KWH/datalogger/config/datalogger.conf

# Activate 1 minute transmission via cron
sudo mv /KWH/datalogger/moves/dcrond /etc/cron.d/.
sudo chmod 644 /etc/cron.d/dcrond

# Setting up SIM communications on ttyAMA0
sudo systemctl mask serial-getty@ttyAMA0.service

# Adjusting /boot/config.txt for SIM and Temp sensors communications
sudo cp /boot/config.txt /KWH/.
sudo chown pi:pi /KWH/config.txt
echo "
#Data Logger
dtoverlay=pi3-disable-bt
enable_uart=1
force_turbo=1
dtoverlay=w1-gpio" >> /KWH/config.txt
sudo cp /KWH/config.txt /boot/config.txt
rm /KWH/config.txt

#Install minimal modbus
cd /KWH/datalogger/lib/MinimalModbus-0.7
sudo ./setup.py build
sudo ./setup.py install
