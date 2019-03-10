#!/usr/bin/env python
import sys
sys.path.append('/kwh/lib')
import KWH_MySQL

# load kwh environment variables from config
DPATH = "/kwh"
execfile(DPATH + "/config/load_config.py")
timestamp = sys.argv[1]+" "+sys.argv[2]

# build database object
DB = KWH_MySQL.KWH_MySQL()

# setup the transmission string (tx_string)
tx_string = config_var['ADMPW']+"#STA:" + config_var['STA'] + ";TM:"
data = DB.SELECT("SELECT `key`, value FROM data WHERE time_created = \""+timestamp+"\";")

# modify timestamp for tx_string (removing all non-numbers for later parsing)
timestamp = timestamp[:4]+timestamp[5:7]+timestamp[8:10]+timestamp[11:13]+timestamp[14:16]+timestamp[17:19]
tx_string += timestamp
for pair in data:
    tx_string += ";" + str(pair[0]) + ":" + str(pair[1])

# Finish string
tx_string += "#" 

# Write to tstring
with open(DPATH + '/transceive/tcp/tstring', 'w') as tstring:
    tstring.write(tx_string)

# Write to tx_string table
sql = "INSERT INTO tx_string VALUES (\"" + timestamp + "\",\"" + tx_string + "\", 0)"
results = DB.INSERT(sql)
