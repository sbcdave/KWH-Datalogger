#!/bin/bash
/KWH/datalogger/adc/capture.py
echo "capture: $?" > /KWH/datalogger/transceive/tcp/transmit.log
/KWH/datalogger/datetime/datetime.py
echo "datetime: $?" >> /KWH/datalogger/transceive/tcp/transmit.log
/KWH/datalogger/transceive/tcp/tstring.py
echo $'\cZ' >> /KWH/datalogger/transceive/tcp/tstring
echo "tstring: $?" >> /KWH/datalogger/transceive/tcp/transmit.log
. /KWH/datalogger/transceive/tcp/tcpSend.sh >> \
/KWH/datalogger/transceive/tcp/transmit.log 2>&1
echo "tcpSend: $?" >> /KWH/datalogger/transceive/tcp/transmit.log
