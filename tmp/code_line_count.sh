#!/bin/bash
find /KWH/* ! -path '/KWH/lib*' -a ! -path '/KWH/other*' -a ! -path '/KWH/UNLIC*' -a ! -path "*.log" -name '*' ! -path "/KWH/helpful_pdfs/*" | xargs wc -l

