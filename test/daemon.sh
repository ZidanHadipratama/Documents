#!/bin/bash

cleanup() {
    exit 0
}

trap 'cleanup' EXIT INT TERM

if [ -t 0 ]; then
    setsid "$0" "$@" </dev/null >/dev/null 2>&1 &
    exit 0
fi

while true; do
    sleep 60
done
