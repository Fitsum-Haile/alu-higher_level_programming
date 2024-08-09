#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument from the database
hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Ensure that the correct number of arguments are provided
    if len(sys.argv) != 4:
        sys.exit(1)

    # Parse command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create an engine and a session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query the state with the provided name
        state = session.query(State).filter(State.name == state_name).first()

        # Print the result or "Not found" if no state matches
        if state:
            print(state.id)
        else:
            print("Not found")
    except Exception as e:
        # Print an error message if there is an issue with the database query
        print(f"Error: {e}")
    finally:
        # Close the session
        session.close()
