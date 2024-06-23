#!/usr/bin/python3

"""script that lists all states from the database """

import MySQLdb
import sys

if __name__ == "__main__":

    user, pwrd, dbase, n = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=pwrd,
            db=dbase,
            charset="utf8")
    cur = conn.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (n,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
