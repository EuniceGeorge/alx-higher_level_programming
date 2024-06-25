#!/usr/bin/python3
""" Start link class to table in database """

from sqlalchemy import create_engine, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    Base = declarative_base()
    session = Session()


for state in session.query(State).order_by(State.id)[:5]:
    print("{}: {}".format(state.id, state.name))
session.close()
