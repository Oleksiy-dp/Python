import pyodbc
import datetime
server = '192.168.1.101'
#server = 'localhost'
database = 'SampleDB'
username = 'user'
password = 'pass'
driver= '{ODBC Driver 17 for SQL Server}'
port='1433'

cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT='+port+';DATABASE='+database+';\
##Trusted_Connection=yes;\
UID='+username+';PWD='+password)
cursor = cnxn.cursor()
tsql = "SELECT SUM(Price) as sum FROM Table_with_5M_rows"
a = datetime.now()
with cursor.execute(tsql):
  b = datetime.now()
  c = b - a
  for row in cursor:
    print ('Sum:', str(row[0]))
  print ('QueryTime:', c.microseconds, 'ms')
  