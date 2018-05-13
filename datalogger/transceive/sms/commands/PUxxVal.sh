#!/bin/bash

path="/KWH/datalogger/pulse/PU0"$1
echo -n "$2" > $path
echo "$2 > $path" > /KWH/datalogger/transceive/sms/commands/PUxxVal.log
