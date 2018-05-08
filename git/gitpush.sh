#!/bin/bash

#To push code up
cd /KWH
git init
wait
echo $(expr $(cat /KWH/datalogger/config/gitV2) + 1) > /KWH/datalogger/config/gitV2
wait
version="v$(cat /KWH/datalogger/config/gitV1).$(cat /KWH/datalogger/config/gitV2)"
wait
git add .
wait
git commit -m $version
wait
git push -v origin master
