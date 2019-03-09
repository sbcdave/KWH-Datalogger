#!/usr/bin/env python
# DO NOT MODIFY THIS FILE - USE setconf alias or /KWH/datalogger/config/setConf.sh

#pip install MySQL-python
#pip install mysql-connector-python
#pip install pymysql

#new edits
import mysql.connector
from mysql.connector import Error
try:
	conn = mysql.connector.connect(host='localhost',
					database = 'datalogger',
					user = 'pi',
					password='')
	cursor = conn.cursor()
	cursor.execute("SELECT `key`, `value` FROM `config` WHERE `active`=1")
	records = cursor.fetchall()

	config_var = {} #dictionary for config vars
	for row in records:
		config_var[row[0]] = row[1]

except Error as e:
	print(e)
finally:
	if conn.is_connected():
		cursor.close()
		conn.close()

#end of new edits
