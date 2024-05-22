#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    __models = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        dictionary = {}
        if cls:
            if type(cls) is type:
                cls = get_key_from_value(self.__models, cls)
            for key, val in self.__objects.items():
                if key.split(".")[0] == cls:
                    dictionary.update({key: val})
            return dictionary
        dictionary.update(FileStorage.__objects)
        return dictionary

    def new(self, obj):
        """Adds new object to storage dictionary"""
        FileStorage.__objects.update(
                    {obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        self.__models = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }

        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.__objects[key] = self.__models[
                        val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete obj from __objects if it’s inside if obj not in __objects,
            the method this method does nothing

        Args:
            obj (_type_, optional): obj to be deleted.
        """
        if obj:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def close(self):
        """
        Reloads the storage dictionary from a file.
        """
        self.reload()


def get_key_from_value(dictionary, target_value):
    """
    Get the key associated with a given value in a dictionary.

    This function iterates through the dictionary and returns the first key
    that has the specified target value. If no such key is found,
    it returns None.

    Parameters:
    dictionary (dict): The dictionary to search through.
    target_value: The value for which to find the corresponding key.

    Returns:
    The key associated with the target value if found, otherwise None.
    """
    for key, value in dictionary.items():
        if value == target_value:
            return key
    return None
