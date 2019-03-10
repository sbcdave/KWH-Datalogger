#!/bin/bash

# Start pigpio daemon
sudo /usr/local/pigpio/util/pigpiod start

# Start all pulse listeners
/KWH/pulse/PU01.py &
/KWH/pulse/PU02.py &
/KWH/pulse/PU03.py &
/KWH/pulse/PU04.py &
/KWH/pulse/PU05.py &
/KWH/pulse/PU06.py &
/KWH/pulse/PU07.py &
/KWH/pulse/PU08.py &
