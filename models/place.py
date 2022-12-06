#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from os import getenv
from sqlalchemy.orm import relationship
from models.review import Review


place_amenity = Table('place_amenity', Base.metadata,
                      Column("amenity_id", String(60), ForeignKey(
                          "amenities.id"), primary_key=True, nullable=False),
                      Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False), extend_existing=True)


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer(), default=0, nullable=False)
    number_bathrooms = Column(Integer(), default=0, nullable=False)
    max_guest = Column(Integer(), default=0, nullable=False)
    price_by_night = Column(Integer(), default=0, nullable=False)
    latitude = Column(Float())
    longitude = Column(Float())
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship(
        "Amenity", secondary_association=place_amenity, viewonly=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            from models import storage
            return [rev for rev in list(storage.all(Review).values())
                    if rev.place_id == self.id]

        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity
            return [amet for amet in list(storage.all(Amenity).values())
                    if amet.id == self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            if value is not None:
                self.amenity_ids.append(value.id)
