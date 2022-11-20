from house_rental import *
from house_purchase import *
from apartment_rental import *
from apartment_purchase import *

class Agent:
    class_dict = {('house', 'rental'): HouseRental, ('house', 'purchase'): HousePurchase, ('apartment', 'rental'): ApartmentRental,('apartment', 'purchase'): ApartmentPurchase }

    def __init__(self):
        self.__property_list = []
    
    def add_property(self):
        property_type = get_valid_input('Property Type', ('house', 'apartment')).lower()
        payment_type  = get_valid_input('Payment Type' , ('purchase', 'rental')).lower()
        item = None
        if property_type == 'house' and payment_type == 'rental': 
            item = HouseRental()
        elif property_type == 'house' and payment_type == 'purchase': 
            item = HousePurchase()
        elif property_type == 'apartment' and payment_type == 'purchase': 
            item = ApartmentPurchase()
        elif property_type == 'apartment' and payment_type == 'rental': 
            item = ApartmentRental()
        self.__property_list.append(item)

    def show_all_properties(self):
        for obj in self.__property_list: print(obj)
    
    def show_match_properties(self):
        property_type = get_valid_input('Property Type', ('house', 'apartment')).lower()
        payment_type  = get_valid_input('Payment Type' , ('purchase', 'rental')).lower()
        for obj in self.__property_list:
            if Agent.class_dict[property_type,payment_type] == type(obj):
                print(obj)

    def modify_properties(self):
        index = int(input(f'Enter Number from 1 to {len(self.__property_list)}: '))
        if index < 1 or index > len(self.__property_list):
            print('INVALID INPUT!')
        else:
            obj = self.__property_list[index-1]
            obj.set_modify_values()

