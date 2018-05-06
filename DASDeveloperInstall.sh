#!/bin/bash

echo ""
echo "This script installs hub to simplify DAS development via GitHub"
echo "Credit https://github.com/github/hub.git and Google"
echo "Downloading GoLang for hub install..."
echo ""
wget https://dl.google.com/go/go1.10.2.linux-armv6l.tar.gz
wait
echo "Unpacking Go..."
tar -C /usr/local -xzf /KWH/go1.10.2.linux-armv6l.tar.gz
wait
echo ""
echo "Moving Go binary to a location that is in \$PATH"
sudo cp /usr/local/go/bin/go /usr/sbin/go
wait
echo ""
echo "Deleting tar.gz"
rm /KWH/go1.10.2.linux-armv6l.tar.gz
wait
echo ""
echo "Downloading hub into /usr/local ..."
cd /usr/local
wait
sudo git clone https://github.com/github/hub.git
wait
echo ""
echo "Installing hub..."
cd /usr/local/hub
./script/build
wait
echo ""
echo "Moving hub binary to a location that is in \$PATH"
sudo cp /usr/local/hub/bin/hub /usr/sbin/hub
wait
echo ""
echo "Aliasing hub as git..."
echo eval \"\$\(hub alias -s\)\" >> ~/.bashrc
wait
echo ""
echo "Setting up git config"
echo "Please enter GitHub email address:"
read email
echo "Is this correct: $email \(y/n\)?"
read ans
if [ "$ans" = "y" ]; then
    git config --global user.email $email
fi
echo "Please enter Name for GitHub commits:"
read name
echo "Is this correct: $name \(y/n\)?"
read ans
if [ "$ans" = "y" ]; then
    git config --global user.name $name
fi
echo "Use \"git config\" for help on resetting these values, or edit the file ~/.gitconfig"
echo ""
echo "Finished! You need to reload your .bashrc file with \". ~/.bashrc\", or reboot"
echo "with \"sudo shutdown -r now\""
