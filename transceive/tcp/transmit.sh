#!/bin/bash

sudo systemctl stop simserver.service
wait

/usr/sbin/sakis3g connect --console
wait

/kwh/transceive/tcp/transmit.py
wait

/usr/sbin/sakis3g disconnect --console
wait

sudo systemctl start simserver.service
wait
