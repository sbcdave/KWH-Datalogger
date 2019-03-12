#!/bin/bash
echo 'SELECT * FROM kwh.data WHERE `key` like "'$1%\" | mysql -u pi
