#!/usr/bin/env python
# DO NOT MODIFY THIS FILE - USE setconf alias or /KWH/datalogger/config/setConf.sh

#pip install MySQL-python
#pip install mysql-connector-python
#pip install pymysql

#new edits
import mysql.connector
from mysql.connector import Error
""" Connect to MySQL database """
try:
	conn = mysql.connector.connect(host='localhost',
					database = 'datalogger',
					user = 'pi',
					password='')
	if conn.is_connected():
		print('Connected to MySQL datalogger database')
	cursor = conn.cursor()
	#cursor.execute("SELECT COUNT(*) FROM config WHERE active=1")
	cursor.execute("SELECT `key`, `value` FROM `config` WHERE `active`=1")
	records = cursor.fetchall()

	configVars = {} #dictionary for config vars
	for row in records:
		configVars[row[0]] = row[1]

except Error as e:
	print(e)
finally:
	if conn.is_connected():
		cursor.close()
		conn.close()
		print('Connection to MySQL datalogger database is closed')

#end of new edits
