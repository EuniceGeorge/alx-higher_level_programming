#!/usr/bin/python3
""" Start link class to table in database """
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

#engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    #sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
#Session = sessionmaker(bind=engine)

#Base.metadata.create_all(engine)


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)


#session = Session()
#for state in session.query(State).order_by(State.id).all():
    #print("{}: {}".format(state.id, state.name))
#session.close()
