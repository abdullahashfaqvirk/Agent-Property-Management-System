from apartment import *
from rental import *

class ApartmentRental(Apartment, Rental):
    def __init__(self):
        super().__init__()
        Rental.__init__(self)
    
    def __str__(self):
        return super().__str__() + Rental.__str__(self)

    def set_modify_values(self):
        super().set_values()
        Rental.set_values_rental(self)
