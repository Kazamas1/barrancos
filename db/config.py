import sqlalchemy

dbname="postgres"
user="eugeni"
password="Lapices1"
host="barrancos.c0qwag6sjhn6.us-east-1.rds.amazonaws.com"
port='5432'

DATABASE_URI = 'postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(user, password,host, port,dbname)

tabase_connection = sqlalchemy.create_engine(DATABASE_URI).connect()
print(tabase_connection)

tabase_connection.close