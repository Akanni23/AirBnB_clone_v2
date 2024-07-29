#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import (Column, String, ForeignKey, Float, Integer)

from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """ 
    A place to stay 
    """
    __tablename__ = 'Places'
    city_id = Column(string(60), ForeignKey('ciites.id'), nullable=False)
    user_id = Column(string(60), ForeignKey('user.id'), nullable=False)
    name = Column(string(128), nullable=False)
    description = Column(string(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
