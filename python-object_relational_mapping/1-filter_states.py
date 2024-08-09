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
    # Connect to the MySQL database using credentials from command line args
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Execute SQL query to fetch states with names starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows returned by the query
    rows = cur.fetchall()

    # Print each row in the specified format
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states()
