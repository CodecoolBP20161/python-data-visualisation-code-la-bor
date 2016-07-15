import psycopg2
import subprocess


class ConnectDatabase:
    # setup connection string
    with open('connect_str.txt', "r") as f:
        connect_str = f.readline()
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()

    @classmethod
    def run_query(cls, query):
        cls.cursor.execute(query)
        rows = cls.cursor.fetchall()
        return rows
