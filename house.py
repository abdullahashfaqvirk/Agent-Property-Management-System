from functions import get_valid_input
from property import *

class House(Property):
    valid_garage = ('attached', 'detached', 'none')
    valid_fenced = ('yes', 'no')

    def __init__(self):
        self.set_values()
    
    def __str__(self):
        s = "<<<<< HOUSE DETAILS >>>>>\n"
        s += f"Garage Type: {self.__garage}\n"
        s += f"Is Fenced: {self.__fenced}\n"
        s += f"No. of Stories: {self.__stories}\n"
        return super().__str__() + s

    def set_values(self):
        super().set_values()
        self.__garage = get_valid_input("Garage Type", House.valid_garage)
        self.__fenced = get_valid_input("Is Fenced", House.valid_fenced)
        self.__stories = input('No. of Stories: ')

