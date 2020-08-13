#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE make_model_pol (
            full_vhl_cd varchar(20),
            full_vhl_cname varchar(50),
            vhl_type varchar(10),
            maker_jv varchar(20),
            maker_cd varchar(20),
            full_maker_cname varchar(50),
            brand_cname varchar(20),
            brand_cd varchar(20),
            model_cd varchar(20),
            model_cd_jy varchar(20), 
            register_year varchar(20),
            vhl_capacity double precision
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        ## empty query issue here.
        ## run above command in pgAdmin4 instead
        for command in commands:
            if command !="":
                cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
