import mysql.connector
from mysql.connector import errorcode

try:
        cnx = mysql.connector.connect(host ='172.17.10.64', user='java', pass$
        cursor = cnx.cursor()
        query = "SELECT * FROM test"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
                print(row[0])
except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with user/paswd")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
        else:
                print(err)
else:
        cnx.close()
