#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, Integer, String, DateTime, Float, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from models.amenity import Amenity

class Place(BaseModel, Base):
    """The place class"""
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place")
    amenities = relationship("Amenity", secondary="place_amenity",
                             back_populates="place_amenities")

    metadata = Base.metadata

    place_amenity = Table(Amenity, metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
               primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
               primary_key=True, nullable=False),
        )
  
    @property
    def reviews(self):
        """returns list of reviews with shared place id"""
        return self.reviews
   
    @property
    def amenities(self):
        """getter for amenities"""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, amenities):
        """setter for amenities"""
        self.aenities_ids.append(amenities)
        return self.amenity_ids
