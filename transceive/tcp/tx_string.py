#!/usr/bin/env python
import sys
sys.path.append('/kwh/lib')
import KWH_MySQL

# load kwh environment variables from config
DPATH = "/kwh"
execfile(DPATH + "/config/load_config.py")
timestamp = sys.argv[1]

# build database object
DB = KWH_MySQL.KWH_MySQL()

# setup the transmission string (tx_string)
tx_string = config_var['ADMPW']+"#STA:" + config_var['STA'] + ";TM:"+timestamp
data = DB.SELECT("SELECT `key`, value FROM data WHERE timestamp = "+timestamp+";")

for pair in data:
    tx_string += ";" + str(pair[0]) + ":" + str(pair[1]).rstrip("0")

# Finish string
tx_string += "#" 

# Write to tx_string table
if config_var['COMPRESS'] == "1":
    import zlib
    tx_string = zlib.compress(tx_string, 6)

with open("/kwh/transceive/tcp/txstring", "w") as file:
    file.write(tx_string)

# Escape any " in the compressed string to faciliate the insert
tx_string = tx_string.replace('"', '\\"')
sql = "INSERT INTO tx_string VALUES (" + timestamp + ",\"" + tx_string + "\");"
results = DB.INSERT(sql)
