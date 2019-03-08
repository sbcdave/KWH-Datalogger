#!/usr/bin/env python
import bitbang

# load datalogger environment variables from config
DPATH = "/KWH/datalogger"
#execfile(DPATH + "/config/pyvars.py")

################################################################################
# 1. The RPi GPIO pins for the ADC are hard coded into bitbang.py
################################################################################
# 2. The ADC has 12 bits and upon request from the RPi it responds with numbers 
# from 0 to 4095. If the sensed voltage = the comparison voltage, the ADC will 
# respond with 4095. If the sensed voltage is half the comparison voltage, the 
# ADC will respond with 2048.
# i.e. ADC reported voltage = (x/4096) * comparison voltage, where x is the 
# number the ADC responds with.
################################################################################
# 3. Not every request the pi sends to the ADC gets an accurate response. With a 
# large enough set of respones, the majority are accurate. This logic takes a 
# set of samples and orders them from smallest to largest. Placing the set in 
# numerical order puts the low and high outliers at the beggining and end of the
# array. The logic then looks at the middle of the array and computes a mean 
# average.
# e.g. Logic asks for 7 samples and the chip responds with: 
#      1002, 45, 1007, 4003, 4095, 1008, 2
# These are ordered to: 2, 45, 1002, 1007, 1008, 4003, 4095
# Then logic takes a mean average of the center three: (1002 + 1007 + 1008) / 3
# 1005.666 is then divided by 4095 to see the ratio of the comparison voltage.
# The logic then uses the equation from (2.) to report the voltage...~1.25 V
################################################################################

import mysql.connector
from mysql.connector import Error
""" Connect to MySQL database """
try:
        conn = mysql.connector.connect(host = 'localhost',
                                        database = 'datalogger',
                                        user = 'pi',
                                        password = '')
        cursor = conn.cursor()
	
	cursor.execute("SELECT `value` FROM `config` WHERE `key` = 'AD01' AND `active` = 1")
        AD01 = cursor.fetchone()[0]
	cursor.execute("SELECT `value` FROM `config` WHERE `key` = 'AD02' AND `active` = 1")
        AD02 = cursor.fetchone()[0]
	cursor.execute("SELECT `value` FROM `config` WHERE `key` = 'AD03' AND `active` = 1")
        AD03 = cursor.fetchone()[0]
	cursor.execute("SELECT `value` FROM `config` WHERE `key` = 'AD04' AND `active` = 1")
        AD04 = cursor.fetchone()[0]
	cursor.execute("SELECT `value` FROM `config` WHERE `key` = 'AD05' AND `active` = 1")
        AD05 = cursor.fetchone()[0]
	cursor.execute("SELECT `value` FROM `config` WHERE `key` = 'AD06' AND `active` = 1")
        AD06 = cursor.fetchone()[0]
	cursor.execute("SELECT `value` FROM `config` WHERE `key` = 'AD07' AND `active` = 1")
        AD07 = cursor.fetchone()[0]
	cursor.execute("SELECT `value` FROM `config` WHERE `key` = 'AD08' AND `active` = 1")
        AD08 = cursor.fetchone()[0]

except Error as e:
        print(e)

samples = 31
cmpr_voltage = 5.25
skewing_percentage = 1.0
bias = 0.000

# instantiating needed arrays
value = []
channel = []
config = [AD01, AD02, AD03, AD04, AD05, AD06, AD07, AD08]

# collecting samples in 2-d array: value x channel
for j in range(8):
    if config[j] == '1':
	for i in range(samples):
		# using this because unable to append 1st element
		if i == 0:
			value = [bitbang.readadc(j)]
		else:
			value.append(bitbang.readadc(j))
	# using this because unable to append 1st element
	if j == 0:
		channel = [sorted(value)]
	else:
		channel.append(sorted(value))

# computing responses and storing in values[]
#grabbing the middle third of the data to ignore outliers
values = [0]*8
for i in range(8):
    if config[i] == '1':
	values[i] = (channel[i][len(channel[i])/2-2] + \
		    channel[i][len(channel[i])/2-1] + \
		    channel[i][len(channel[i])/2] + \
		    channel[i][len(channel[i])/2+1] + \
		    channel[i][len(channel[i])/2+2]) / 5
    else:
	values[i] = 0.0

# read the datetime from datetime
with open(DPATH + '/datetime/datetime', 'r') as dt:
        datetime = dt.read()

# compute the values
for i in range(8):
    if config[i] == '1':
	values[i] = (values[i]/4095.0)*cmpr_voltage*skewing_percentage-bias
        # insert into data table
        sql_insert = "INSERT INTO `data` VALUES ('"+datetime+"', 'A"+str(i+1)+"', "+str(values[i])+");"
        print(sql_insert)
        try:
            cursor.execute(sql_insert)
            conn.commit()
        except Error as e:
            print(e)
if conn.is_connected():
    cursor.close()
    conn.close()
