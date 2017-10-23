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

# Do stuff, e.g.
#    if [ ! -z "$1" ] && [ ! -z "$2" ]; then
#	/KWH/datalogger/transceive/send_at.sh +CMGF=1; \
#	sleep 2
#	/KWH/datalogger/transceive/send_at.sh +cmgs=\"$1\"$'\n'${@: -`expr $# - 1`}$'\cZ'
#    else
#        echo "Usage: send <phone number> <message>"
#    fi



    # standard cleanup on proper exit so we never leave the lock file around
    cleanup $PROGNAME
}
main $*
