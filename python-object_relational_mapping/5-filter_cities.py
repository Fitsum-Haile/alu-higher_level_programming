#!/usr/bin/python3
"""
Module 5-filter_cities
Lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def filter_cities_by_state():
    """
    Displays all cities of a given state, sorted by city id
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    # SQL query with parameterized input to prevent SQL injection
    query = ("SELECT cities.name FROM cities JOIN states "
             "ON cities.state_id = states.id WHERE states.name = %s "
             "ORDER BY cities.id")
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()

    # Extracting city names and joining them with commas
    cities = ", ".join([row[0] for row in rows])
    print(cities)

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_cities_by_state()
