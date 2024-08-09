#!/usr/bin/python3
"""
Module 2-my_filter_states
Displays all states in the states table matching the user input
"""

import MySQLdb
import sys


def filter_states_by_user_input():
    """
    Displays all states with a name that matches the argument,
    sorted by id
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    # Create SQL query with user input, using format to insert state name
    query = ("SELECT * FROM states WHERE BINARY name = '{}' "
             "ORDER BY id ASC".format(sys.argv[4]))

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states_by_user_input()
