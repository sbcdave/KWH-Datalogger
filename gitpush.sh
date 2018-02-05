#!/bin/bash

#To push code up
cd /KWH
git init
git add .
git commit -m "v`expr $(cat version) + 1`" &&
cat $(expr $(cat version) + 1) > version
git push -v origin master
