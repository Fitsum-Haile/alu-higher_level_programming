#!/usr/bin/python3
"""State class for SQLAlchemy ORM."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base

class State(Base):
    """State class mapped to the states table with cities relationship."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
