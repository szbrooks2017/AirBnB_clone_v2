#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """getter for cities"""
        from models import storage
        get_cities = []
        for k, v in storage.all(City).items():
            if v.state_id == self.id:
                get_cities.append(v)
        return get_cities
