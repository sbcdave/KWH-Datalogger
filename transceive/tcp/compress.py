#!/usr/bin/env python3
import socket
import sys
sys.path.append('/kwh/lib')
import KWH_MySQL
import zlib

# load config variables from kwh.config table
exec(open("/kwh/config/get_config.py").read())

data = sys.argv[1]
bytedata = bytearray()
bytedata = zlib.compress(data, 6)
