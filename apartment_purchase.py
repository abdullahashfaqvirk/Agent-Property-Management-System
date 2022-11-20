from apartment import *
from purchase import *

class ApartmentPurchase(Apartment, Purchase):
    def __init__(self):
        super().__init__()
        Purchase.__init__(self)

    def __str__(self):
        return super().__str__() + Purchase.__str__(self)
    
    def set_modify_values(self):
        super().set_values()
        Purchase.set_values_purchase(self)
