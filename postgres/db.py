
import psycopg2



def connect_bd():
    conn=psycopg2.connect(dbname='postgres', user='postgres',password='RunForestNN[12]',host='localhost')
    cursor =conn.cursor()
    return cursor