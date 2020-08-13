#!/usr/bin/python3

""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
import models
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = ""
