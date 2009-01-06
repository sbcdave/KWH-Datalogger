#!/bin/bash

# Seconds from Jan 1 1900 (Network Time Protocol epoch) to Jan 1 1970 (Unix epoch)
timeShift=2208988800

sudo date -s @$(($((0x$(xxd -ps /KWH/datalogger/datetime/nisttime))) - $timeShift)) >> /KWH/datalogger/datetime/datetime.log
