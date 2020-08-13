#!/usr/bin/python
import csv
import psycopg2
from config import config
import sys
def insert_make_model_list(file_to_read):
    """ insert multiple make&model records into the make_model_pol table  """
    tablename='pol_dz'
    fieldnames = ('id1', 'id2', 'renew_or_not', 'unknown_name1', 'major_line', 'minor_line',
'province', 'city', 'unknown_name2', 'channel1', 'channel2', 'unknown_name17','unknown_name18','inception_date',
'expire_date','unknown_date1','unknown_date2','vhl_plate_typ','unknown_name19','brand_cname', 'unknown_name3',
'register_date', 'unknown_name4','unknown_name5','unknown_name6','unknown_name7','unknown_name8',
'unknown_name9','unknown_name10','unknown_name11','unknown_name12', 'id3', 'id4', 'unknown_name13','birth_date', 'gender', 'contract_date', 'unknown_name14', 'unknown_name15', 'cur_vhl_price', 'orig_vhl_price','id5', 'unknown_name16')
    sql = f'INSERT INTO {tablename} ({",".join(fieldnames)}) VALUES({", ".join(["%s"]*len(fieldnames))})'
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        with open(file_to_read, 'r', encoding='gb18030') as f:
            csv_reader = csv.reader(f, delimiter='|')
            for record in csv_reader:
        # execute the INSERT statement    
                cur.executemany(sql, [record])
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
    insert_make_model_list(sys.argv[1])
