#!/bin/bash

#To push code up
cd /KWH
git init
git add .
git commit -m "v`expr $(cat /KWH/version) + 1`" &&
echo $(expr $(cat /KWH/version) + 1) > /KWH/version
git push -v origin master
