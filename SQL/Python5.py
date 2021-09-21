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

print ('Отобразить водителей у кторых совпадает страна проживания и страна доставки. которые прживают в городах начинающихся на Be, возраст больше 22 лет. Отсортировать по LastName')
print ('_____________________________________________________')
print ('DriverLastName| DriverFirstName| Country | City | Age ')

cursor.execute('''SELECT
dr.[DriverLastName]
,dr.[DriverFirstName]
,dr.[Country] 
,dr.[City]
,YEAR(GETDATE()) - Year(dr.BirthDate) as Age
  FROM [CargoTrans].[dbo].[Customers] Cus JOIN	Orders O ON Cus.CustomerID = O.CustomerID
  JOIN CargoDetails CD ON O.OrderID = CD.OrderID
  JOIN Drivers Dr ON cd.DriverID = Dr.DriverID
  WHERE dr.Country = o.ShipCountry AND dr.City LIKE 'Be%'
  AND (YEAR(GETDATE()) - Year(dr.BirthDate)) > 22
  ORDER BY dr.DriverLastName''')

for row in cursor:
    print(row)




