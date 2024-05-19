#!/usr/bin/python3
"""
State Module for HBNB project

This code snippet defines a class called State. It is a subclass of
the BaseModel class and the Base class from the SQLAlchemy library.
The State class represents a state in the HBNB project.

Attributes:
- __tablename__: A string representing the name of the table in
    the database where instances of the State class will be stored.
- name: A string representing the name of the state. This attribute
    is required and cannot be null.
- cities: A relationship attribute representing the relationship between
    the State class and the City class. It defines a one-to-many relationship,
    where one state can have multiple cities. The relationship is defined
    using the SQLAlchemy ORM.

Methods:
- cities(): A getter method for the cities attribute. It returns the cities
    associated with the state.

Note: The behavior of the code snippet depends on the value of the environment
variable HBNB_TYPE_STORAGE. If it is set to "db", the State class will have
additional attributes and a relationship with the City class. Otherwise,
the name attribute will be an empty string.

"""


from models.base_model import Base, BaseModel
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        name = ''

    @property
    def cities(self):
        """
        Getter method for cities.
        Retrieves a list of City objects associated with the state.

        Returns:
            List[City]: A list of City objects associated with the state.
        """
        from models import storage
        from models import City

        return [
                city for city in storage.all(City).
                values() if self.id == city.state_id
                ]
