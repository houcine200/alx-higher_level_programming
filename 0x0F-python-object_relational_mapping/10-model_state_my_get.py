#!/usr/bin/python3
"""
prints the State object with the name passed as an argument
from the database `hbtn_0e_6_usa`
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
    """
    state = session.query(State).filter(State.name == argv[4]).all()

    if not state:
        print("Not found")
    else:
        print(state[0].id)
    """
    state = session.query(State).filter(State.name == argv[4]).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)
