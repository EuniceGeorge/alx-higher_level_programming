#!/usr/bin/python3
""" Start link class to table in database """

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ Create the 'states' table. """
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
