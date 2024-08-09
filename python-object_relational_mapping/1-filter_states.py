#!/usr/bin/python3
"""
Module 1-filter_states
Lists all states with a name starting with 'N' from the database
"""

import MySQLdb
import sys


def filter_states():
    """
    Lists all states with a name starting with 'N', sorted by id
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    # Execute SQL query to fetch states with names starting with 'N'
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' "
                "ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states()
