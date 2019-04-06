#!/usr/bin/env python3
import sys
sys.path.append('/kwh/lib')
import KWH_MySQL

DB = KWH_MySQL.KWH_MySQL()

sql = "SELECT `key`, `value` FROM `config` WHERE `active`=1"

records = DB.SELECT(sql)

# dictionary of key:value from kwh.config table
config_var = {} 
for row in records:
    config_var[row[0]] = row[1]
