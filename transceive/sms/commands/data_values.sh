#!/bin/bash

. /kwh/config/kwh.conf

data=$(data)

source /kwh/transceive/sms/smsSend.sh $1 `echo $data`
wait

