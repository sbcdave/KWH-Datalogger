#!/bin/bash

echo ""
echo "This script installs hub to simplify DAS development via GitHub"
echo "Credit https://github.com/github/hub.git and Google"
echo "Downloading GoLang for hub install..."
echo ""
wget https://dl.google.com/go/go1.10.2.linux-armv6l.tar.gz
wait
echo "Unpacking Go..."
tar -xzf /KWH/go1.10.2.linux-armv6l.tar.gz
wait
echo ""
echo "Moving Go binary to a location that is in \$PATH"
sudo cp /KWH/go/bin/go /usr/sbin/.
wait
echo ""
echo "Downloading hub..."
git clone https://github.com/github/hub.git
wait
echo ""
echo "Installing hub..."
/KWH/hub/script/build
wait
echo ""
echo "Aliasing hub as git..."
echo eval \"\$\(hub alias -s\)\" >> ~/.bashrc
. ~/.bashrc
echo "Finished! You may need to reload your .bashrc file"
