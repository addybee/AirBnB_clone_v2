#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """defines amenities

    Args:
        BaseModel (class): parent class
    """
    name = ""
