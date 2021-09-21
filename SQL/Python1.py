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

print ('отобразить Водителей из стран Finland, Italy, Luxembourg , которые не из города Anderson и отсортировать по странам')
#Insert Query
print ('_____________________________________________________')

cursor.execute('''SELECT DISTINCT
           [DriverLastName]
          ,[DriverFirstName]
	  ,[Country]
	  ,City
  FROM [CargoTrans].[dbo].[Drivers]
  WHERE Country IN ('Finland', 'Italy', 'Luxembourg') AND City NOT LIKE 'Anderson'
  GROUP BY Country,City, [DriverLastName]
      ,[DriverFirstName]
  ORDER BY Country''')
for row in cursor:
    print(row)




