import psycopg2


def dbaction(sqlfunction):
    conn = psycopg2.connect(
        database="postgres",
        user="eugeni",
        password="Lapices1",
        host="barrancos.c0qwag6sjhn6.us-east-1.rds.amazonaws.com",
        port='5432'

    )

    print(conn)

    cursor = conn.cursor()

    cursor.execute(sqlfunction)
    cursor.fetchall()

    cursor.close()
   
funciont =  'select 1'
print(dbaction(function))