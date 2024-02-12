#!/usr/bin/python3

class Base():
    
    self.__nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
            self.__nb_objects = id
        elif id == None:
            self.__nb_objects += 1
