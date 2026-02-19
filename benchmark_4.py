<<<<<<< HEAD
import benchmark_2
import benchmark_3

from benchmark_3 import recipe
from customer_class import Customer

customers = []

for i in range(10):
    customers.append(Customer())

for customer in customers:
    atrributes = customer.get_customer_attributes()
    ice_cream_pref = atrributes["ice_Cream"]
    toppings_pref = atrributes["toppings"]
    price_limit = atrributes["price"]

=======
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

>>>>>>> 173a103eb185668c6883a5240bde3d304830b174
