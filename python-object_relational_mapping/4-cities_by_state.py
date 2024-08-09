#!/usr/bin/python3
"""
Module 4-cities_by_state
Lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def list_cities():
    """
    Displays all cities with their state names, sorted by city id
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    # Query to join cities with states and sort by city id
    query = ("SELECT cities.id, cities.name, states.name FROM cities "
             "JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities()
