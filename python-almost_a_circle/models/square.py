#!/usr/bin/python3
""" Class Square """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ Class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The unique identifier of the square.

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)
        
        

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return "[Square]" + " " + "(" + str(self.id) + ")" + " " + str(self.x) + \
            "/" + str(self.y) + " " + "-" + " " + str(self.width)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square.

        Returns:
            None
        """
        self.width = value
        self.height = value
