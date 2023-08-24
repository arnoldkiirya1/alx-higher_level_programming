#!/usr/bin/python3
"""Print the State object with the specified name from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    queried_state = session.query(State).filter(State.name == state_name).first()

    if queried_state:
        print(queried_state.id)
    else:
        print("Not found")

    session.close()

