#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""script that lists all states that starts wwith letter 'N"""

import MySQLdb
import sys

if __name__ == "__main__":

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    conn.close()
