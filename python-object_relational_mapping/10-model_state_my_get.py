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
    if len(sys.argv) != 4:
        print("Usage: ./10-model_state_my_get.py \
<mysql username> <mysql password> <database name> <state name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).filter(State.name == state_name).first()

        if state:
            print(state.id)
        else:
            print("Not found")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()
