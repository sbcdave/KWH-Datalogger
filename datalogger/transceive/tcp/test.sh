#!/bin/bash
    echo AT+CIPSHUT | nc localhost 9999 &
    wait
    echo AT+CGATT=0 | nc localhost 9999 &
    wait
    echo AT+CGATT=1 | nc localhost 9999 &
    wait
    echo AT+CIPSHUT | nc localhost 9999 &
    wait
    echo AT+CIPMUX=0 | nc localhost 9999 &
    wait
    echo AT+CSTT=\"wholesale\" | nc localhost 9999 &
    wait
    echo AT+CIICR | nc localhost 9999 &
    wait
    echo AT+CIFSR | nc localhost 9999 &
    wait
    echo AT+CIPSTART | nc localhost 9999 &
    wait
    echo AT+CIPSEND | nc localhost 9999 &
    wait
    cat /KWH/datalogger/transceive/tcp/tstring | nc localhost 9999 &
    wait
    echo AT+CIPCLOSE | nc localhost 9999 &
    wait
    echo AT+CIPSHUT | nc localhost 9999 &
    wait

