#!/bin/bash
stty -F /dev/ttyAMA0 `cat /KWH/datalogger/conf/sttySettings.tty`
