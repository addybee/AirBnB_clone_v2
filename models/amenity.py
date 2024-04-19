#!/usr/bin/python3
""" State Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from os import getenv


class Amenity(BaseModel, Base):
    """defines amenities

    Args:
        BaseModel (class): parent class
    """
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""
