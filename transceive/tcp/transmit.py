#!/usr/bin/env python
import mysql.connector
from mysql.connector import Error
#from _thread import *
#import threading
import time
import socket
import sys
sys.path.append('/kwh/lib')
import KWH_MySQL

# load kwh environment variables from config
DPATH = "/kwh"
execfile(DPATH + "/config/load_config.py")

# sends tx_string and delete from tx_string if the server responds
#def sender_thread(row):
#    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    server.connect((config_var['DOMAIN'], int(config_var['PORT'])))
#    server.send(row[1])
#    rcv = s.recv(1024)
#    if rcv == row[0]:
#        DB = KWH_MySQL.KWH_MySQL()
#        sql = "DELETE FROM kwh.tx_string WHERE timestamp = " + row[0]
#        result = DB.INSERT(sql)

#    s.close()


# MAIN #
# Grab up to 100 tx_strings and pass them to sender_threads
try:
    conn = mysql.connector.connect(host='localhost',
                                   database = 'kwh',
                                   user = 'pi',
                                   password='')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tx_string LIMIT 100;")
    records = cursor.fetchall()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((config_var['DOMAIN'], int(config_var['PORT'])))
    time.sleep(0.1)
    for row in records:
#        start_new_thread(sender_thread, (row,))
        server.send(row[1])
        time.sleep(0.1)
        rcv = server.recv(1024)
        print(rcv)
        print(row[0])
        if rcv == row[0]:
            DB = KWH_MySQL.KWH_MySQL()
            sql = "DELETE FROM kwh.tx_string WHERE timestamp = " + row[0]
            result = DB.INSERT(sql)
            print(result)
    server.close()

except Error as e:
    print(e)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
