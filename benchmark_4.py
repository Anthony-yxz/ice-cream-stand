import customer_class

from customer_class import Customer


customers = []

for i in range(10):
    customers.append(Customer())

for i in customers:
    attributes = i.get_customer_attributes()
    icecream_pref = attributes["icecream"]
    toppings_pref = attributes["toppings"]
    price_limit = attributes["price"]

