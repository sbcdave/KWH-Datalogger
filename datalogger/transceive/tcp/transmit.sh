#!/bin/bash
/KWH/datalogger/adc/capture.py
echo "capture: $?" > /KWH/datalogger/transceive/tcp/transmit.log
/KWH/datalogger/datetime/datetime.py
echo "datetime: $?" >> /KWH/datalogger/transceive/tcp/transmit.log
/KWH/datalogger/transceive/tcp/tstring.py
echo "tstring: $?" >> /KWH/datalogger/transceive/tcp/transmit.log
. /KWH/datalogger/transceive/tcp/tcpSend.sh
echo "tcpSend: $?" >> /KWH/datalogger/transceive/tcp/transmit.log
