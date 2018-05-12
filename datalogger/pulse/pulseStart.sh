#!/bin/bash

# Start pigpio daemon
sudo /usr/local/pigpio/util/pigpiod start

# Start all pulse listeners
/KWH/datalogger/pulse/PU01.py &
/KWH/datalogger/pulse/PU02.py &
/KWH/datalogger/pulse/PU03.py &
/KWH/datalogger/pulse/PU04.py &
/KWH/datalogger/pulse/PU05.py &
/KWH/datalogger/pulse/PU06.py &
/KWH/datalogger/pulse/PU07.py &
/KWH/datalogger/pulse/PU08.py &
