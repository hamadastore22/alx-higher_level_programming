#!/usr/bin/python3
'''Module for Base class.'''


class Base:
    '''A representation of the base of our oop hirrarcy.'''
    __nb__object =0
    def __init__(self, id=None):
        '''constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=  1
            self.id = Base.__nb_objects