#!/bin/bash
sudo date -s @$(( $(( 2#$( echo $1 | xxd -b | head -c 44 | tail -c 35 | tr -d [:space:]) )) - 2208988800 ))
