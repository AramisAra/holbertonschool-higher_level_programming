#!/usr/bin/python3
""" Base Class """

class Base():
    """
    Base class for all other classes in the project.
    """

    self.__nb_objects = 0
    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): The id of the object. Defaults to None.
        """
        if id != None:
            self.id = id
            self.__nb_objects = id
        elif id == None:
            self.__nb_objects += 1
