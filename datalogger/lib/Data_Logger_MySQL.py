class Data_Logger_MySQL(object):
    def __init__(self):
        True

    def SELECT(self, sql):
        import mysql.connector
        from mysql.connector import Error

        try:
            conn = mysql.connector.connect(host='localhost',database = 'datalogger',user = 'pi',password='')
            cursor = conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()

        except mysql.connector.Error as error:
            return [1, error]

        if conn.is_connected():
            cursor.close()
            conn.close()

        return result

    def INSERT(self, sql):
        import mysql.connector
        from mysql.connector import Error

        try:
            conn = mysql.connector.connect(host='localhost',database = 'datalogger',user = 'pi',password='')
            cursor = conn.cursor()
            result = cursor.execute(sql)
            conn.commit()
            if conn.is_connected():
                cursor.close()
                conn.close()
            
        except mysql.connector.Error as error:
            conn.rollback()
            if conn.is_connected():
                cursor.close()
                conn.close()
            return [1, error]

        return [0]
