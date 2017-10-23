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

    # begin sending commands and logging
    DPATH="/KWH/datalogger/transceive"
    source /KWH/datalogger/conf/datalogger.conf
    echo "/KWH/datalogger/conf/datalogger.conf sourced..." > ${DPATH}/tcp/tcpSend.log

    . ${DPATH}/send_at.sh +cipshut &&
    echo "Waiting on AT+CIPSHUT..." >> ${DPATH}/tcp/tcpSend.log
    sleep 4 &&
    wait

    $(echo "AT+CFUN=0" > ${DPATH}/tcp/at_input.txt; \
echo "AT+CFUN=1" >> ${DPATH}/tcp/at_input.txt; \
echo "AT+CGATT=1" >> ${DPATH}/tcp/at_input.txt;) &&
    atinout ${DPATH}/tcp/at_input.txt /dev/ttyAMA0 - >> \
${DPATH}/tcp/tcpSend.log &&
    wait

#    $(echo "AT+CGATT=1" > ${DPATH}/tcp/at_input.txt;) &&
#    atinout ${DPATH}/tcp/at_input.txt /dev/ttyAMA0 - >> \
#${DPATH}/tcp/tcpSend.log &&

    . ${DPATH}/send_at.sh +cipmux=0 &&
    echo "Waiting on AT+CIPMUX=0..." >> ${DPATH}/tcp/tcpSend.log
    sleep 4 &&
    wait

    $(echo "AT+CSTT=\"$APN\"" > ${DPATH}/tcp/at_input.txt; \
echo "AT+CIICR" >> ${DPATH}/tcp/at_input.txt; \
echo "AT+CIFSR" >> ${DPATH}/tcp/at_input.txt; \
echo "AT+CIPSTART=\"TCP\",\"$DOMAIN\",\"$PORT\"" >> \
${DPATH}/tcp/at_input.txt;) &&
    atinout ${DPATH}/tcp/at_input.txt /dev/ttyAMA0 - >> \
${DPATH}/tcp/tcpSend.log &&

    . ${DPATH}/send_at.sh +cipsend &&
    sleep 4 &&

    cat ${DPATH}/tcp/tstring > /dev/ttyAMA0 &&
    sleep 1 &&
    echo -n $'\cZ' > /dev/ttyAMA0 &&
    sleep 1 &&
    . ${DPATH}/send_at.sh +cipclose &&
    sleep 1 &&
    . ${DPATH}/send_at.sh +cipshut


    # standard cleanup on proper exit so we never leave the lock file around
    cleanup $PROGNAME
}
main $*
