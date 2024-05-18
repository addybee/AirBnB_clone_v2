#!/usr/bin/python3
""" This module defines a class to manage DB storage for hbnb clone """


from typing import Dict, Optional
from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """
    The DBStorage class manages the database storage and operations in a
    Flask application.
    It uses SQLAlchemy to interact with the MySQL database.
    """

    __engine = None
    __session = None
    __models = {}

    def __init__(self):
        """
        Initializes the DBStorage instance by setting up the database
        connection and session.
        It also drops all tables if the environment is set to "test".
        """
        mysql_user = os.getenv("HBNB_MYSQL_USER")
        mysql_pass = os.getenv("HBNB_MYSQL_PWD")
        mysql_host = os.getenv("HBNB_MYSQL_HOST")
        mysql_DB = os.getenv("HBNB_MYSQL_DB")
        mysql_env = os.getenv("HBNB_ENV")
        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(mysql_user,
                                                      mysql_pass,
                                                      mysql_host,
                                                      mysql_DB)
        self.__engine = create_engine(db_url, pool_pre_ping=True, echo=False)
        meta = MetaData()
        if mysql_env == "test":
            try:
                meta.drop_all(self.__engine)
            except SQLAlchemyError:
                pass

    def all(self, cls: Optional[type] = None) -> Dict[str, object]:
        """
        Retrieves all objects from the database session.
        If a class is specified, it retrieves objects of that class only.

        Args:
            cls (optional): The class of objects to retrieve.

        Returns:
            A dictionary of objects.
        """
        dict_obj = {}
        try:
            session = self.__session()
            if cls:
                for obj in session.query(cls).all():
                    dict_obj.update(
                        {obj.to_dict()['__class__'] + '.' + obj.id: obj})
            else:
                for cls in self.__models.values():
                    if cls != self.__models["BaseModel"]:
                        for obj in session.query(cls).all():
                            dict_obj.\
                                update({obj.to_dict()['__class__'] + '.'
                                        + obj.id: obj})
        except SQLAlchemyError as e:
            print(f'Error occurred: {str(e)}')

        return dict_obj

    def new(self, obj):
        """
        Adds a new object to the database session.

        Args:
            obj: The object to be added to the database session.

        Returns:
            None
        """
        session = self.__session()
        session.add(obj)

    def save(self) -> None:
        """
        Commits all changes made in the current database session.
        """
        session = self.__session()
        session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the database session.

        Args:
            obj (optional): The object to be deleted from the database session

        Returns:
            None
        """
        session = self.__session()
        if obj:
            session.delete(obj)

    def reload(self):
        """
        Reloads the database session by recreating the metadata and
        session objects.
        This method should be called when you want to refresh the
        session and ensure that any changes made to the database are
        reflected in the session.
        """
        from models.base_model import Base
        from models import user, state, city, amenity, place, review

        self.__models = {'State': state.State, 'City': city.City,
                         'User': user.User, 'Place': place.Place,
                         'Review': review.Review, 'Amenity': amenity.Amenity,
                         }
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """
        Closes the current database session.
        This method should be called when you are done using the session to
        free up resources and prevent any potential issues.
        """
        self.__session.close()
