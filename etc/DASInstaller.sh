#!/bin/bash

# Intro
echo ""
echo "================================================================================"
echo "=   Welcome to the KiloWatts for Humanity (KWH) Data Logger software package   ="
echo "================================================================================"
echo ""
echo "Thank you for your interest, and enjoy! Courtesy of KiloWatts for Humanity (KWH)"
echo ""
echo "This installer requires that the RPi be rebooted when complete"
echo "If you need to save any work, do not answer anything that starts with \"y\""
echo ""
echo "Would you like to continue with installation(y/n)?"
read ans
if [ "${ans:0:1}" != "y" ]; then
    echo ""
    echo "Exiting...Relaunch the DASInstaller.sh when you are ready."
    echo "Courtesy of KiloWatts for Humanity"
    echo ""
    exit
fi

# Install git for pulling the code from the repository
echo ""
echo "Verifying installation of and/or Installing git"
wait
sudo apt-get install -y git
status=$?
wait
if [ $status -ne 0 ]; then
    echo "unable to access git...aborting"
    echo "contact dave@KiloWattsforHumanity.org for assistance"
fi

# Move to root and download data logger code from github
cd /
echo ""
echo "Downloading data logger software to the root directory in /KWH"
wait
sudo git clone https://github.com/sbcdave/KWH.git
status=$?
wait
if [ $status -ne 0 ]; then
    echo ""
    echo "GitHub download stalled...rerun DASInstaller.sh"
    echo ""
    exit
fi

# Download pigpio code from github
cd /
echo ""
echo "Downloading pigpio code to /KWH/lib"
wait
cd /KWH/lib
git clone https://github.com/joan2937/pigpio.git
status=$?
wait
if [ $status -ne 0 ]; then
    echo ""
    echo "GitHub download stalled...rerun DASInstaller.sh"
    echo ""
    exit
fi

# Change data logger code root directory owner:group to pi
echo ""
echo "Updating /KWH permissions"
wait
sudo chown -R pi:pi KWH
wait

#investigate shutting down uneccesary services

# Create symlink from /etc/defaults to datalogger.conf file
echo ""
echo "Ensuring datalogger config is used at boot and setting auto-login to console"
wait
sudo ln -n /KWH/config.conf /etc/default.conf
wait
# Add datalogger.conf file to root and pi's .bashrc
sudo cp /KWH/moves/.bashrc /root/.bashrc
wait
cp /KWH/moves/.bashrc /home/pi/.bashrc
wait
# Source the aliases functions and environment variables
. ~/.bashrc
wait
sudo cp /KWH/moves/autologin@.service /etc/systemd/system/autologin@.service
wait
sudo systemctl daemon-reload
wait
sudo systemctl enable autologin@.service
wait

# Setting up SIM communications on ttyAMA0
echo ""
echo "Enabling ttyAMA0 on TX/RX for SIM comms"
wait
sudo systemctl mask serial-getty@ttyAMA0.service
wait

# Adjusting /boot/config.txt for SIM and Temp sensors communications
echo ""
echo "Updating /boot/config.txt to enable SIM and Temp sensor comms"
wait
sudo cp /KWH/moves/config.txt /boot/config.txt
wait

# Enable simserver.service
echo ""
echo "Enabling sim server service"
sudo cp /KWH/moves/simserver.service /etc/systemd/system/.
wait
sudo systemctl enable simserver.service
wait

# Enable simserver.service
echo ""
echo "Enabling pigpiod service"
sudo cp /KWH/moves/pigpiod.service /etc/systemd/system/.
wait
sudo systemctl enable pigpiod.service
wait

# Enable simserver.service
echo ""
echo "Enabling get time service"
sudo cp /KWH/moves/gettime.service /etc/systemd/system/.
wait
sudo systemctl enable gettime.service
wait

# Switching keyboard layout to US
echo ""
echo "Switching keyboard layout to US standard"
echo "Use \"sudo raspi-config\" if you would like to change it"
sudo cp /KWH/moves/keyboard /etc/default/keyboard

# Activate 1 minute transmission via cron
echo ""
echo "Enabling cron jobs for reading sms, transmitting data, and updating the time"
wait
sudo cp /KWH/moves/dcrond /etc/cron.d/dcrond
wait
sudo chmod 644 /etc/cron.d/dcrond
wait

# Reboot to finalize
echo ""
echo "Installation complete. We will soon reboot to enable communications with the PCB or other hardware solution."
echo ""
echo "If you would like KWH to host your data, please contact dave@kilowattsforhumanity.org"
echo "You can donate to KiloWatts for Humanity at http://kilowattsforhumanity.org"
echo "We hope you enjoy!"
echo ""
echo "Rebooting now is highly recommended as some communications will be erroring and filling log files"
echo "However, if you need to stop the reboot, you can use \"ctrl+c\" to kill the program without reboot"
echo "Press enter to reboot now..."
read ans
sudo shutdown -r now
