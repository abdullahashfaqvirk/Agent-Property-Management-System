class Property:
    def __init__(self):
        self.set_values()

    def __str__(self):
        s = "\n<<<<< PROPERTY DETAILS >>>>>\n"
        s += f"Area (square feet): {self.__sq_feet}\n"
        s += f"No. of Bedrooms : {self.__no_bedrooms}\n"
        s += f"No. of Bathrooms: {self.__no_bathrooms}\n\n"
        return s

    def set_values(self):
        self.__sq_feet = input('Total Area (square feet): ')
        self.__no_bedrooms = input('No. of Bedrooms: ')
        self.__no_bathrooms = input('No. of Bathrooms: ')
