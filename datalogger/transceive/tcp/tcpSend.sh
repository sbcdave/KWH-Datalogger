#!/bin/bash

readonly PROGNAME=$(basename "$0")
readonly LOCKFILE_DIR=/tmp
readonly LOCK_FD=200

lock() {
    local prefix=$1
    local fd=${2:-$LOCK_FD}
    local lock_file=$LOCKFILE_DIR/$prefix.lock

    # create lock file
    eval "exec $fd>$lock_file"

    # acquier the lock
    flock -n $fd \
        && return 0 \
        || return 1
}

ttrap() {
    local func="$1"; shift
    for sig in "$@"; do
        trap "$func $sig" "$sig"
    done
}

trap_recurse() {
    local signal=$1

    # deregister trap for this signal (trap recursion)
    trap - $signal
    # kill any child processes in this group, passing on same signal
    kill -s $signal "-$$"
}

cleanup() {
    local prefix=$1
    local signal=$2

    local lock_file=$LOCKFILE_DIR/$prefix.lock

    # cleanup lock_file
    rm -f "$lock_file"

    if [[ -n "$signal" ]]; then
        trap_recurse $signal
    fi
}

eexit() {
    local error_str="$@"

    echo $error_str
    exit 1
}

main() {
    # trap signals
    ttrap "cleanup $PROGNAME" SIGHUP SIGINT SIGQUIT SIGTERM

    lock $PROGNAME \
        || eexit "Only one instance of $PROGNAME can run at one time."

    # set DPATH for reference to shorten script
    DPATH="/KWH/datalogger/transceive"

    # source envvars and aliases for use in script
    . /KWH/datalogger/conf/datalogger.conf

    # configure tty settings for baud rate, parity, etc...
    stty -F /dev/ttyAMA0 `cat /KWH/datalogger/conf/sttySettings.tty`

    # begin log
    echo "/KWH/datalogger/conf/datalogger.conf sourced..." > ${DPATH}/tcp/tcpSend.log

    # initiate IP SHUT for cleanup
    echo AT+CIPSHUT > /dev/ttyAMA0
    echo "Waiting 2s on AT+CIPSHUT..." >> ${DPATH}/tcp/tcpSend.log
    sleep 2

    # software reset via funtion disable/enable (CFUN) and
    # (detach from GSM) / (attach to GSM)
    $(echo "AT+CFUN=0" > ${DPATH}/tcp/at_input.txt; \
echo "AT+CFUN=1" >> ${DPATH}/tcp/at_input.txt; \
echo "AT+CGATT=0" >> ${DPATH}/tcp/at_input.txt; \
echo "AT+CGATT=1" >> ${DPATH}/tcp/at_input.txt;)
    atinout ${DPATH}/tcp/at_input.txt /dev/ttyAMA0 ${DPATH}/tcp/atinout.tmp &&
    cat ${DPATH}/tcp/atinout.tmp >> ${DPATH}/tcp/tcpSend.log

    # Shut again for CIPMUX switch to work, not sure why!
    echo AT+CIPSHUT > /dev/ttyAMA0
    echo "Waiting 2s on AT+CIPSHUT..." >> ${DPATH}/tcp/tcpSend.log
    sleep 2

    # switch to single connection mode
    echo AT+CIPMUX=0 > /dev/ttyAMA0
    echo "Waiting 2s on AT+CIPMUX=0..." >> ${DPATH}/tcp/tcpSend.log
    sleep 2
    
    # set APN and bring up connection to cell tower
    $(echo "AT+CSTT=\"$APN\"" > ${DPATH}/tcp/at_input.txt; echo "AT+CIICR" >> ${DPATH}/tcp/at_input.txt;)
    atinout ${DPATH}/tcp/at_input.txt /dev/ttyAMA0 ${DPATH}/tcp/atinout.tmp &&
    cat ${DPATH}/tcp/atinout.tmp >> ${DPATH}/tcp/tcpSend.log

    # request IP address
    echo AT+CIFSR > /dev/ttyAMA0
    echo "Requesting IP address..." >> ${DPATH}/tcp/tcpSend.log
    sleep 2

    # establish net.tcp// connection to DOMAIN:PORT
    echo "AT+CIPSTART=\"TCP\",\"$DOMAIN\",\"$PORT\"" > ${DPATH}/tcp/at_input.txt
    atinout ${DPATH}/tcp/at_input.txt /dev/ttyAMA0 ${DPATH}/tcp/atinout.tmp
    cat ${DPATH}/tcp/atinout.tmp >> ${DPATH}/tcp/tcpSend.log

    # begin TCP transfer to DOMAIN:PORT
    echo AT+CIPSEND > /dev/ttyAMA0
    echo "Waiting 2s on AT+CIPSEND..." >> ${DPATH}/tcp/tcpSend.log
    sleep 2 

    cat ${DPATH}/tcp/tstring > /dev/ttyAMA0
    echo "Sending transmission string (tstring) with wait 1s..." >> ${DPATH}/tcp/tcpSend.log
    sleep 1

    echo -n $'\cZ' > /dev/ttyAMA0
    echo "Sending ^Z to SIM with wait 1s..." >> ${DPATH}/tcp/tcpSend.log
    sleep 1

    echo AT+CIPCLOSE > /dev/ttyAMA0
    echo "Closing connection. Wait 1..." >> ${DPATH}/tcp/tcpSend.log
    sleep 1

    echo AT+CIPSHUT > /dev/ttyAMA0
    echo "Sent AT+CIPSHUT...Finished" >> ${DPATH}/tcp/tcpSend.log

    # standard cleanup on proper exit so we never leave the lock file around
    cleanup $PROGNAME
}
main $*
