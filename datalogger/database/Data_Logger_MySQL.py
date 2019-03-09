class Data_Logger_MySQL(object):
    def __init__(self):
        import mysql.connector
        from mysql.connector import Error
        """ Connect to MySQL database """
        try:
	    conn = mysql.connector.connect(host='localhost',database = 'datalogger',user = 'pi',password='')
            cursor = conn.cursor()
            #cursor.execute("SELECT COUNT(*) FROM config WHERE active=1")

        except Error as e:
            print(e)

# We may eventually need something like this in a desctructor if the MySQL connections aren't handled by garbage collection
#        finally:
#            if conn.is_connected():
#                cursor.close()
#                conn.close()
#                print('Connection to MySQL datalogger database is closed')

    def Execute_SQL(self, sql, records):
        cursor.execute(sql)
        records = cursor.fetchall()
