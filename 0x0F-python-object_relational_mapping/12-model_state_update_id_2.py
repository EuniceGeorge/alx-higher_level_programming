#!/usr/bin/python3
""" A script that prints the State object
    with the name passed as argument from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy.sql.expression import update

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    obj = session.query(State).get(2)
    print("name: ", obj.name)
    obj.name = 'New Mexico'
    x = session.query(State).first()
    session.commit()
    session.close()
