#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            from models import storage
            """
            Returns the list of City instances
            with state_id equals to the current State.id
            """
            lst = []
            Objs = storage.all(City)
            for k, v in Objs.items():
                if k == 'state_id':
                    if v == self.id:
                        lst.append(v)
            return lst
