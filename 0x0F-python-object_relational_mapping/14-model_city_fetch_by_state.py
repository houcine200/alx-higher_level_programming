#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""
from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City)\
        .join(State, State.id == City.state_id).all()

    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")
