#!/usr/bin/python3
""" A script that prints the State object
    with the name passed as argument from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_obj = State(name='Louisiana')

    session.add(state_obj)
    session.commit()
    print("{:d}".format(state_obj.id))
    session.close()
