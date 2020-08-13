#!/usr/bin/python
import csv
import psycopg2
from config import config

def insert_make_model_list(make_model_list):
    """ insert multiple make&model records into the make_model_dz table  """
    sql = "INSERT INTO make_model_dz(auto, line, branch_name2, vhl_code_jy, make_model, rlt_mm) VALUES(%s, %s, %s, %s, %s, %s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, make_model_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    # insert multiple vendors
    if False:
    # if True:
        insert_make_model_list([
            ('private', 'phd', '上海', 'ADAAE', '奥迪A4', '0.8'),
            ('private', 'phd', '上海', 'ADAAF', '奥迪A6', 0.9),
            ('private', 'phd', '上海', 'ADAAG', '奥迪A8', 0.85),
            ('private', 'phd', '上海', 'ADAAI', '奥迪Q7', 0.85)
        ])
    # if False:
    if True:
        with open('make_model.csv', 'r', encoding='gb2312') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            insert_make_model_list([tuple(record.values()) for record in csv_reader])