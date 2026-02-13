import customer_class

from customer_class import Customer


customers = []

for i in range(10):
    customers.append(Customer())

for i in customers:
    attributes = i.get_customer_attributes()
    Ice_Cream_pref = attributes["Icecream"]
    toppings_pref = attributes["toppings"]
    price_limit = attributes["price"]
