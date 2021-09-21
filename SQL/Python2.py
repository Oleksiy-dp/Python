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

print ('отобразить водителей у которых совпадает страна проживания со страной выдачи лицензии и их возраст менее 37 лет')
print ('_____________________________________________________')

cursor.execute('''SELECT  
       d.[DriverLastName]
      ,d.[DriverFirstName]
	  ,d.[Country]
	  ,d.City
	  ,l.City AS CityLic
	  ,YEAR(GETDATE()) - Year(d.BirthDate) as Age
	  FROM [CargoTrans].[dbo].[Drivers] D JOIN DriversLicense L ON D.DriverID = L.DriverID 
	WHERE d.Country = l.Country AND (YEAR(GETDATE()) - Year(d.BirthDate)) < 37
    ORDER BY d.Country''')
for row in cursor:
    print(row)




