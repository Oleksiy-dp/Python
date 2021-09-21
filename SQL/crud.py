import pyodbc
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

print ('Inserting a new row into table')
#Insert Query
tsql = "INSERT INTO Employees (Name, Location) VALUES (?,?);"
with cursor.execute(tsql,'Jake','United States'):
    print ('Successfully Inserted!')


#Update Query
print ('Updating Location for Nikita')
tsql = "UPDATE Employees SET Location = ? WHERE Name = ?"
with cursor.execute(tsql,'Sweden','Nikita'):
    print ('Successfully Updated!')


#Delete Query
print ('Deleting user Jared')
tsql = "DELETE FROM Employees WHERE Name = ?"
with cursor.execute(tsql,'Jared'):
    print ('Successfully Deleted!')


#Select Query
print ('Reading data from table')
tsql = "SELECT *  FROM [SampleDB].[dbo].[Employees];"
with cursor.execute(tsql):
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()
