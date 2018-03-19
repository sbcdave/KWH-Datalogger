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

    . /KWH/datalogger/conf/datalogger.conf

    echo AT+CMGF=1 | nc localhost $SIM_PORT \
	> /KWH/datalogger/transceive/sms/delete.txt
    echo AT+CMGD=$1 | nc localhost $SIM_PORT \
	>> /KWH/datalogger/transceive/sms/delete.txt

    # standard cleanup on proper exit so we never leave the lock file around
    cleanup $PROGNAME
}
main $*
