#!/bin/bash

sudo systemctl stop simserver.service
wait

sudo /bin/sakis3g connect --console
wait

sudo /kwh/transceive/tcp/transmit.py
wait

sudo /bin/sakis3g disconnect --console
wait

sudo systemctl start simserver.service
wait
