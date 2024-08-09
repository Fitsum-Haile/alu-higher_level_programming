#!/usr/bin/python3
"""
Module 3-my_safe_filter_states
Displays all states in the states table matching the user input
Safeguarded against SQL injections
"""

import MySQLdb
import sys


def safe_filter_states():
    """
    Displays all states with a name that matches the argument,
    sorted by id, safe from SQL injection
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    # Use parameterized query to avoid SQL injection
    query = ("SELECT * FROM states WHERE BINARY name = %s "
             "ORDER BY id ASC")
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states()
