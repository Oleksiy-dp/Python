import pyodbc
server = '192.168.1.101'
#server = 'localhost'
database = 'CargoTrans'
username = 'user'
password = 'pass'
driver= '{ODBC Driver 17 for SQL Server}'
port='1433'

cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT='+port+';DATABASE='+database+';\
##Trusted_Connection=yes;\
UID='+username+';PWD='+password)
cursor = cnxn.cursor()

print ('Отобразить компании у кого Freight больше среднего')
print ('_____________________________________________________')

cursor.execute('''SELECT c.[CompanyName],c.[ContactName]
  FROM [CargoTrans].[dbo].[Customers] C, Orders O
  WHERE C.CustomerID = O.CustomerID
    AND o.Freight > 
(SELECT
AVG(Freight)
from Orders)''')
for row in cursor:
    print(row)




