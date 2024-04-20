#!/usr/bin/python3
""" This module defines a class to manage DB storage for hbnb clone """


from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {
            'BaseModel': BaseModel, 'State': State, 'City': City,
            'User': User, 'Place': Place,
            'Review': Review, 'Amenity': Amenity,
            }


class DBStorage:
    """ """
    __engine = None
    __session = None

    def __init__(self):
        """ """
        mysql_user = os.getenv("HBNB_MYSQL_USER")
        mysql_pass = os.getenv("HBNB_MYSQL_PWD")
        mysql_host = os.getenv("HBNB_MYSQL_HOST")
        mysql_DB = os.getenv("HBNB_MYSQL_DB")
        mysql_env = os.getenv("HBNB_ENV")
        DBStorage.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                           format(mysql_user,
                                                  mysql_pass,
                                                  mysql_host,
                                                  mysql_DB),
                                           pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if mysql_env == "test":
            try:
                Base.metadata.drop_all(self.__engine)
            except SQLAlchemyError as e:
                pass

    def all(self, cls=None):
        """ """
        dict_obj = {}
        try:
            session = self.__session()
            if cls:
                for obj in session.query(cls).all():
                    dict_obj.update(
                        {obj.to_dict()['__class__'] + '.' + obj.id: obj})
            else:
                for cls in classes.values():
                    if cls != classes["BaseModel"]:
                        for obj in session.query(cls).all():
                            dict_obj.\
                                update({obj.to_dict()['__class__'] + '.'
                                        + obj.id: obj})
        except SQLAlchemyError as e:
            pass

        return dict_obj

    def new(self, obj):
        """ """
        session = self.__session()
        session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        session = self.__session()
        session.commit()

    def delete(self, obj=None):
        """ """
        session = self.__session
        if obj:
            session.delete(obj)

    def reload(self):
        """ """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session
