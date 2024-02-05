#!/usr/bin/python3
"""
This is a docstring for the Rectangle class.
"""

class Rectangle:
    """
    This is a docstring for the Rectangle class.
    """
    def __init__(self, width=0, height=0):
        """
        This adding the need atributtes
        """
        self.__width = width
        self.__height = height

    def height(self):
        """
        This is a docstring for the height method.
        """
        return self.__height

    def height(self, value):
        """
        This is a docstring for the height setter method.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def width(self):
        """
        This is a docstring for the width method.
        this returns self.__width
        """
        return self.__width

    def width(self, value):
        """
        This is a docstring for the width setter method.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
