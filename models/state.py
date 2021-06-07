#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
    
    @property
    def cities(self):
        """getter for cities"""
        get_cities = []
        for k,v in models.storage.all(City).items():
            if v.state_id == self.id:
                get_cities.append(v)
        return get_cities
