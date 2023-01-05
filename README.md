# Real Estate Application

Welcome to the Real Estate application, a tool for agents to manage properties available for purchase or rent. This application allows agents to enter new properties, list currently available properties, and modify existing properties.

There are two types of properties in this application: apartments and houses. Each property has the following data members:

* square feet
* number of bedrooms
* number of baths

Houses have the additional data members:

* garage
* fenced
* number of stories

Apartments have the additional data members:

* balcony
* laundry

In addition to these data members, rentals and purchases have separate representation. Rentals have the following data members:

* furnished
* rent
* utilities

Purchases have the following data member:

* price
* taxes

# Classes

The following classes have been defined in this application:

* Property: the base class representing a property. It has member functions __init__, __str__, and set_values to initialize, convert to string, and set the values of a property, respectively.
* House: a child class of Property representing a house. It has the same member functions as Property, as well as additional class level members valid_garage and valid_fenced to validate input values for the data members garage and fenced.
* Apartment: a child class of Property representing an apartment. It has the same member functions as Property, as well as additional class level members valid_laundries and valid_balconies to validate input values for the data members laundry and balcony.
* Rental: a class representing a rental property. It has the data members furnished, rent, and utilities, and has member functions __init__, __str__, and set_values to initialize, convert to string, and set the values of a rental property, respectively.
* Purchase: a class representing a property for purchase. It has the data members price and taxes, and has member functions __init__ and __str__ to initialize and convert to string, respectively.
* HouseRental, HousePurchase, ApartmentRental, ApartmentPurchase: each of these classes represents a specific type of property and inherits from both a Property class and either a Rental or Purchase class. They have an __init__ function that calls the __init__ functions of their parent classes.
* Agent: the class representing an agent. It has the data member property_list, a list of all properties, and the class level member class_dict, a dictionary mapping tuples of property type and payment type to the corresponding class. It has member functions __init__ to initialize the list, add_property to add a new property, show_all_properties to display all properties, show_match_properties to display properties matching a given property type and payment type, modify_property to modify an existing property, and remove_property to remove a property.

# Getting Started

To use this application, create an instance of the Agent class and use its member functions to add, modify, and remove properties. The show_all_properties and show_match_properties functions can be used to view the properties in the agent's list
