#!/bin/bash
find /KWH/* ! -path '/KWH/datalogger/libs*' -a ! -path '/KWH/datalogger/other*' -a ! -path '/KWH/UNLIC*' -a ! -path "*.log" -name '*' | xargs wc -l

