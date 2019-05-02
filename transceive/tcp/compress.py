#!/usr/bin/env python3
import socket
import sys
sys.path.append('/kwh/lib')
import KWH_MySQL
import zlib

data = sys.argv[1]
bytedata = bytearray()
bytedata = zlib.compress(data, 6)
