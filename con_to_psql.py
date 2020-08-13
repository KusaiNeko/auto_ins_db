#!/usr/bin/python
import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        # print('PostgreSQL database version:')
        print('My PostgreSQL operations:')

        # cur.execute('SELECT count(*) from make_model_dz')
        # cur.execute('SELECT * from make_model_dz;')
        # rows = cur.fetchall()
        # print('Numer of rows selected:', cur.rowcount)

        # for row in rows:
        #     print(row[3])
        
        # if some changes, need to commit
        cur.execute('DELETE from make_model_dz')
        # commit the changes to the database
        conn.commit()
        print('Numer of rows deleted:', cur.rowcount)
        # cur.execute('SELECT count(*) from make_model_dz')

        # display the PostgreSQL database server version
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        # print(conn.dsn)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
