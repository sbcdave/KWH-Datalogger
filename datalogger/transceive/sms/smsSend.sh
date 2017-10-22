#!/bin/bash
if [ ! -z "$1" ] && [ ! -z "$2" ]; then
	sudo flock -x /KWH/datalogger/conf/SIM_LOCK \
/KWH/datalogger/transceive/send_at.sh +cmgs=\"$1\"$'\n'${@: -`expr $# - 1`}$'\cZ'
else
	echo "Usage: send <phone number> <message>"
fi
