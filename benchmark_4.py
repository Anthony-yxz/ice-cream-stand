import customer_class

from customer_class import Customer


customers = []

for i in range(10):
    customers.append(Customer())

for i in customers:
    attributes = i.get_customer_attributes()
    sweetness_pref = attributes["ice_Cream"]
    ice_pref = attributes["toppings"]
    price_limit = attributes["price"]

