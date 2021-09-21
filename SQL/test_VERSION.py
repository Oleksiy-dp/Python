import pyodbc
import datetime
server = '192.168.1.101'
#server = 'localhost'
database = 'master'
username = 'user'
password = 'pass'
driver= '{ODBC Driver 17 for SQL Server}'
port='1433'

cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT='+port+';DATABASE='+database+';\
##Trusted_Connection=yes;\
UID='+username+';PWD='+password)
cursor = cnxn.cursor()
cursor.execute("SELECT @@VERSION;")
row = cursor.fetchone()
while row:
	print(row)
	row = cursor.fetchone()
