#!/bin/bash
find /KWH/* ! -path '/KWH/datalogger/lib*' -a ! -path '/KWH/datalogger/other*' -a ! -path '/KWH/UNLIC*' -a ! -path "*.log" -name '*' ! -path "/KWH/helpful_pdfs/*" | xargs wc -l

