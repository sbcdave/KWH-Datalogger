#!/bin/bash

readonly PROGNAME=$(basename "$0")
readonly LOCKFILE_DIR=/tmp
readonly LOCK_FD=200

lock() {
    local prefix=$1
    local fd=${2:-$LOCK_FD}
    local lock_file=/KWH/datalogger/conf/SIM_LOCK

    # create lock file
    eval "exec $fd>$lock_file"

    # acquier the lock
    flock -n $fd \
        && return 1 \
        || return 0
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

    while $(lock $PROGNAME)
    do
	sleep 1
    done

    SIM_PORT=9999

    . /KWH/datalogger/conf/datalogger.conf

    echo AT+CMEE=2 | nc localhost ${SIM_PORT} &&
    sleep 2
    echo AT+CIPSHUT | nc localhost ${SIM_PORT} &&
    sleep 2
    echo AT+CGATT=0 | nc localhost ${SIM_PORT} &&
    sleep 2
    echo AT+CGATT=1 | nc localhost ${SIM_PORT} &&
    sleep 2
    echo AT+CIPSHUT | nc localhost ${SIM_PORT} &&
    sleep 2
    echo AT+CIPMUX=0 | nc localhost ${SIM_PORT} &&
    sleep 2
    echo AT+CSTT=\"wholesale\" | nc localhost ${SIM_PORT} &&
    sleep 2
    echo AT+CIICR | nc localhost ${SIM_PORT} &&
    sleep 2
    echo AT+CIFSR | nc localhost ${SIM_PORT} &&
    sleep 2
    echo AT+CIPSTART=\"TCP\",\"time.nist.gov\",\"37\" | nc localhost ${SIM_PORT} &&
    sleep 2
    /KWH/datalogger/datetime/setTime.sh $(grep -A4 'AT+CIPSTART="TCP","time.nist.gov","37"' /KWH/datalogger/transceive/tcp/SIMComs.log | tail -c 6 | head -c 4) &&
    sleep 3
    echo AT+CIPCLOSE | nc localhost ${SIM_PORT} &&
    sleep 2
    echo AT+CIPSHUT | nc localhost ${SIM_PORT}

    # standard cleanup on proper exit so we never leave the lock file around
    cleanup $PROGNAME
}
main $*
