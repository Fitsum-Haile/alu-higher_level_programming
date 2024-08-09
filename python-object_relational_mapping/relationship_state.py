#!/usr/bin/python3
"""Module defining the State class with SQLAlchemy ORM."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base

class State(Base):
    """State class for SQLAlchemy ORM."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    
    # Define relationship with City
    cities = relationship('City', back_populates='state',
            cascade='all, delete-orphan')
