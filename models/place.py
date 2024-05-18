#!/usr/bin/python3
""" Place Module for HBNB project """


from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import ForeignKey, String, Column, Integer, Float, Table
from sqlalchemy.orm import relationship


if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey('places.id'), primary_key=True),
                          Column("amenity_id", String(60),
                                 ForeignKey('amenities.id'), primary_key=True)
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'))
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade="all, delete",
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 cascade="all",
                                 viewonly=False,
                                 backref="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ """
            from models import storage
            from models.review import Review

            review_dict = storage.all(Review)
            return [obj for obj in review_dict.values()
                    if obj.place_id == self.id]

        @property
        def amenities(self):
            """ """
            from models import storage
            from models.amenity import Amenity

            amenity_dict = storage.all(Amenity)
            return [obj
                    for obj in amenity_dict.values()
                    if obj.id in self.amenity_ids
                    ]

        @amenities.setter
        def amenities(self, obj):
            """ """
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
