# customer_class.py
# The customer class represents a customer at the lemondade stand.
# The customer has preferences for ice cream flavor and toppings,
# and a price point they are willing to pay.
# All of these attributes will influence their purchasing decision and
# are returned as a list of attributes.

import random


class Customer:
    def __init__(self, ice_cream_preference=None, toppings_preference=None, price_point=None):
        self.ice_cream_preference = (
            ice_cream_preference if ice_cream_preference is not None
            else random.randint(1, 3)
        )
        self.toppings_preference = (
            toppings_preference if toppings_preference is not None
            else random.randint(0, 3)
        )
        self.price_point = (
            price_point if price_point is not None
            else round(random.uniform(0.25, 4.0),2)
        )

    def get_customer_attributes(self):
        return {
            "Ice_Cream": self.ice_cream_preference,
            "Toppings": self.toppings_preference,
            "price": self.price_point
        }