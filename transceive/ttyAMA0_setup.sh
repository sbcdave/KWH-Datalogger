#!/bin/bash
stty -F /dev/ttyAMA0 `cat /KWH/config/sttySettings.tty`
