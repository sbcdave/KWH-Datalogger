#!/bin/bash

readonly PROGNAME=$(basename "$0")
readonly LOCKFILE_DIR=/tmp
readonly LOCK_FD=200

lock() {
    local prefix=$1
    local fd=${2:-$LOCK_FD}
    local lock_file=/KWH/datalogger/config/SIM_LOCK

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

    . /KWH/datalogger/config/datalogger.conf

    echo AT+CSQ | nc localhost $SIM_PORT > /KWH/datalogger/signal/signal.log
    wait
    echo -n $(grep '\+CSQ:' /KWH/datalogger/signal/signal.log | sed -E 's/\+CSQ: ([0-9]*),.*/\1/') > /KWH/datalogger/signal/signal

    # standard cleanup on proper exit so we never leave the lock file around
    cleanup $PROGNAME
}
main $*
