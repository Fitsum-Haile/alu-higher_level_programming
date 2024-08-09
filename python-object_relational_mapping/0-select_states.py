#!/usr/bin/python3
"""
Module 0-select_states
Connects to a MySQL database and lists all states
"""

import MySQLdb
import sys


def list_states():
    """
    Lists all states in the hbtn_0e_0_usa database, sorted by id
    """
    # Connect to the MySQL database using credentials from command line args
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Execute SQL query to fetch all states, sorted by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the query
    rows = cur.fetchall()

    # Print each row in the specified format
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
