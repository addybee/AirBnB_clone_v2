#!/usr/bin/python3
""" City Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, String, Column
from os import getenv
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id', ondelete='CASCADE'), nullable=False)
        places = relationship("Place", cascade="all, delete",
                              backref="cities")
    else:
        state_id = ""
        name = ""
