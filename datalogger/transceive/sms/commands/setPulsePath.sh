#!/bin/bash

path="/KWH/datalogger/pulse/PU0${1}"
echo -n "${2}" > ${path}
