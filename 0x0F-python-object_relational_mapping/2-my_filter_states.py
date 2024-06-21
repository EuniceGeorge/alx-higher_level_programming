#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""script that lists all states from the database """

import MySQLdb
import sys

if __name__ == "__main__":

    username, password, database, n_searched = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM states WHERE name = '{n_searched}' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
