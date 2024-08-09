#!/usr/bin/python3
"""A script that deletes all State objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <mysql username> "
              "<mysql password> <database name>")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        engine = create_engine(
            f"mysql+mysqldb://{username}:{password}@localhost/{database}",
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query and delete states
        states_to_delete = session.query(State).filter(
            State.name.contains('a')
        ).all()
        for state in states_to_delete:
            session.delete(state)

        session.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    main()
