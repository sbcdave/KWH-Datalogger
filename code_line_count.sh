#!/bin/bash
find /KWH/* ! -path '/KWH/datalogger/lib*' -a ! -path '/KWH/datalogger/other*' -a ! -path '/KWH/UNLIC*' -a ! -path "*.log" -name '*' | xargs wc -l

