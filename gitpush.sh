#!/bin/bash

#To push code up
cd /KWH
git init
echo $(expr $(cat /KWH/datalogger/config/VERSION) + 1) > /KWH/datalogger/config/VERSION
git add .
git commit -m "v$(cat /KWH/datalogger/config/VERSION)" &&
git push -v origin master
