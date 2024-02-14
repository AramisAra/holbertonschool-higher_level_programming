#!/usr/bin/python3
""" Base Class """

import json
class Base():
    """
    Base class for all other classes in the project.
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): The id of the object. Defaults to None.
        """

        type(self).__nb_objects += 1
        self.id = type(self).__nb_objects
        if id != None:
            self.id = id
            __nb_objects = id
            type(self).__nb_objects -= 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_objs = [object.to_dictionary() for object in list_objs]
                jsonfile.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string.

        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new instance of the class and update its attributes.

        Args:
            dictionary (dict): A dictionary of attributes.

        Returns:
            object: A new instance of the class.
        """
        if dictionary and dictionary != {}:
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
