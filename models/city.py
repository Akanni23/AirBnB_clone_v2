#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, String, 
from models.base_model import BaseModel, Base


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ ='cities'
    state_id = Column(String(128), nullable=False)
    name = Column(String(60), ForeignKey('state.id'), nullable=False)
    place = relationship('place', backref='cities', cascade='all, delete-orphan')
