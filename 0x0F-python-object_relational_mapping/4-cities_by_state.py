#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""script that lists all states from the database """

import MySQLdb
import sys

if __name__ == "__main__":

    user, pwrd, dbase = sys.argv[1], sys.argv[2], sys.argv[3]
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=pwrd,
            db=dbase,
            charset="utf8")
    cur = conn.cursor()
    cur.execute(
            "SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
