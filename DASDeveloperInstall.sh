#!/bin/bash

echo "This script installs hub for to simplify development via GitHub"
echo "Credit https://github.com/github/hub.git"
echo "Downloading GoLang for hub install..."
wget https://dl.google.com/go/go1.10.2.linux-armv6l.tar.gz
wait
echo "Unpacking Go..."
tar -xzf go1.10.2.linux-armv61.tar.gz
wait
echo "Moving Go binary to a location that is in \$PATH"
sudo cp /KWH/go/bin/go /usr/sbin/.
wait
echo "Downloading hub..."
git clone https://github.com/github/hub.git
wait
echo "Installing hub..."
/KWH/hub/script/build
wait
echo "Aliasing hub as git..."
echo eval \"\$\(hub alias -s\)\" >> ~/.bashrc
. ~/.bashrc
echo "Finished! You may need to reload your .bashrc file"
