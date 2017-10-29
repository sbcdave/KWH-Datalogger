sudo date -s @$(( $(( 2#$(nc time.nist.gov 37 | xxd -b | head -c 44 | tail -c 35 | tr -d [:space:]) )) - 2208988800 ))
