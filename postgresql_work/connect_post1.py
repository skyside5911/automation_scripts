import psycopg2
connect_database=psycopg2.connect(
    host='localhost',
    dbname='Raj',
    user='postgres',
    password='Karnal@123',
    port=5432
)
print("yes")
connect_database.close()