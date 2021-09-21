import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

server = 'HOME-PC\MSSQLEXPRESS' 
database = 'NORTHWND' 
# username = 'myusername' 
# password = 'mypassword'
# so you have to use in connect: ;UID='+username+';PWD='+ password

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
    SERVER='+server+';DATABASE='+database +'; Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('''SELECT A.LastName AS EmployeesLN
,A.FirstName AS EmployeesFN
,B.LastName AS ManagerLN
,B.FirstName AS ManagerFN
FROM Employees A, Employees B
WHERE a.ReportsTo = b.EmployeeID''')

for row in cursor:
    print(row)
