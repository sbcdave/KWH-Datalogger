#!/usr/bin/env python

import sqlite3

#set constant values
config_sqliteFile = '/KWH/datalogger/config/dataloggerDB.db'

#connect to an existing database
#if not exist, automatically create one
db = sqlite3.connect(config_sqliteFile) #this is the connection
cur = db.cursor()
print "Opened database successfully";

#create a table and insert data
db.execute("
