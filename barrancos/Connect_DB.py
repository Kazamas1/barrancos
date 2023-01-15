import pyodbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = '192.168.0.16:1433'
DATABASE_NAME = 'Torrentes'
"""
connection_string = ''' 
    DRIVER = 'SQL SERVER';
    SERVER = '192.168.0.16:1433';
    DATABASE= 'Torrentes';
    Trust_Connection=yes;
    uid='Eugeni';
    pwd='Ventana1'
'''
print (connection_string)
"""
conn = pyodbc.connect( 'DRIVER={SQL Server};SERVER=192.168.0.16;DATABASE=Torrentes;Trust_Connection=yes')
print(conn)

cursor = conn.cursor()

cursor.execute("select * from Barrancos")
cursor.fetchall()

cursor.close()