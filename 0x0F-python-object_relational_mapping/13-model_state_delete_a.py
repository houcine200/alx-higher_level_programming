#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database `hbtn_0e_6_usa`.
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(State.name.contains("a"))

    for state in states_to_delete:
        session.delete(state)

    session.commit()

    session.close()
