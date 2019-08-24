#!/bin/bash

sudo systemctl stop simserver.service
wait

sudo /kwh/sakis3g/sakis3g connect --console
wait

sudo ntpd -q -g
wait

sudo /kwh/transceive/tcp/transmit.py
wait

sudo /kwh/sakis3g/sakis3g disconnect --console
wait

sudo systemctl start simserver.service
wait
