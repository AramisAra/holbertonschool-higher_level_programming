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
                return []
            return json.dumps(list_dictionaries)
