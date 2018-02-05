#!/bin/bash

#To push code up
cd /KWH
git init
echo $(expr $(cat /KWH/version) + 1) > /KWH/version
git add .
git commit -m "v$(cat /KWH/version)" &&
git push -v origin master
