#!/bin/bash
source /KWH/datalogger/conf/KWH/datalogger.conf
. /KWH/datalogger/transceive/send_at.sh +cfun=0 &&
sleep 2 &&
. /KWH/datalogger/transceive/send_at.sh +cfun=1 &&
sleep 2 &&
. /KWH/datalogger/transceive/send_at.sh +cgatt=0 &&
sleep 3 &&
. /KWH/datalogger/transceive/send_at.sh +cgatt=1 &&
sleep 3 &&
. /KWH/datalogger/transceive/send_at.sh +cipshut &&
sleep 1 &&
. /KWH/datalogger/transceive/send_at.sh +cgatt=1 &&
sleep 1 &&
. /KWH/datalogger/transceive/send_at.sh +cipmux=0 &&
sleep 1 &&
. /KWH/datalogger/transceive/send_at.sh +cstt=\"$APN\" &&
sleep 1 &&
#. /KWH/datalogger/transceive/send_at.sh +cdgcont=1,\"IP\",\"$APN\"
. /KWH/datalogger/transceive/send_at.sh +ciicr &&
sleep 1 &&
. /KWH/datalogger/transceive/send_at.sh +cifsr &&
sleep 1 &&
. /KWH/datalogger/transceive/send_at.sh +cipstart=\"TCP\",\"$DOMAIN\",\"$PORT\" &&
sleep 1 &&
. /KWH/datalogger/transceive/send_at.sh +cipsend &&
sleep 2 &&
head -c 100 /KWH/datalogger/transceive/tcp/tstring > /dev/ttyAMA0 &&
sleep 1 &&
echo -n $'\cZ' > /dev/ttyAMA0 &&
sleep 1 &&
. /KWH/datalogger/transceive/send_at.sh +cipclose &&
slee 1 &&
. /KWH/datalogger/transceive/send_at.sh +cipshut &&
