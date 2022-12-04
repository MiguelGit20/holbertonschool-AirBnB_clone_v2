#!/usr/bin/python3
"""
This module defines a class to manage database storage for hbnb clone.
"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """DBStorage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session
        """
        objects_dict = {}
        if cls is None:
            query = self.__session.query().all()
            for objects in query:
                objects_dict[type(objects).__name__ + '.' +
                             objects.id] = objects
        else:
            query = self.__session.query(cls).all()
            for objects in query:
                objects_dict[type(objects).__name__ + '.' +
                             objects.id] = objects

        return objects_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creating tables and the session"""
        Base.metadata.create_all(self.__engine)
        ssn = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(ssn)
        self.__session = session
