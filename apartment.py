from functions import get_valid_input
from property import *

class Apartment(Property):
    valid_laundries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'solarium')

    def __init__(self):
        self.set_values()
    
    def __str__(self):
        s = "<<<<< APARTMENT DETAILS >>>>>\n"
        s += f"Laundry Type: {self.__laundries}\n"
        s += f"Balcony Type: {self.__balconies}\n"
        return super().__str__() + s

    def set_values(self):
        super().set_values()
        self.__laundries = get_valid_input("Laundries Type", Apartment.valid_laundries)
        self.__balconies = get_valid_input("Balconies Type", Apartment.valid_balconies)

