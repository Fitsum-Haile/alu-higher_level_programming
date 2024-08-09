#!/usr/bin/python3
"""Module defining the State class with SQLAlchemy ORM."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base

class State(Base):
    """State class representing a state in the database."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    
    cities = relationship('City', back_populates='state', 
                          cascade='all, delete-orphan')
