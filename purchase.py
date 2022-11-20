class Purchase:
    def __init__(self):
        self.set_values_purchase()

    def __str__(self):
        s = "\n<<<<< PURCHASE DETAILS >>>>>\n"
        s += f"Total Price: {self.__price}\n"
        s += f"Total Taxes: {self.__taxes}\n"
        return s

    def set_values_purchase(self):
        self.__price = input('Price: ')
        self.__taxes = input('Taxes: ')
