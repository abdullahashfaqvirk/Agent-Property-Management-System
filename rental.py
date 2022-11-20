from functions import get_valid_input

class Rental:
    valid_check = ('yes', 'no')

    def __init__(self):
        self.set_values_rental()

    def __str__(self):
        s = "\n<<<<< RENTAL DETAILS >>>>>\n"
        s += f"Is Furnish: {self.__furnish}\n"
        s += f"Rent: {self.__rent}\n"
        s += f"Utilities: {self.__utilities}\n"
        return s

    def set_values_rental(self):
        self.__furnish = get_valid_input('Is Furnish', Rental.valid_check)
        self.__rent = input('Rent: ')
        self.__utilities = get_valid_input('Utilities Provided', Rental.valid_check)
