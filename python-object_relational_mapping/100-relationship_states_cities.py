#!/usr/bin/python3
"""Script to create State and City in the database using SQLAlchemy."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State


def main():
    """Main function to create State and City entries in the database."""
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <mysql username> "
              "<mysql password> <database name>")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State and City
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    # Add to the session and commit
    session.add(california)
    session.add(san_francisco)
    session.commit()

    session.close()


if __name__ == "__main__":
    main()
