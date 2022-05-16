import pymysql

def MySQLConn():
    return pymysql.connect(host='localhost', user='root', password='let us gou', port=3307, db='comicon')
