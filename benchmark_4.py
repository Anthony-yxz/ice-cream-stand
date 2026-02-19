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

