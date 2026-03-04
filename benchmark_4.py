import time
import benchmark_2
import benchmark_3
from customer_class import Customer

recipe = benchmark_3.recipe
price_per_item = benchmark_3.price_per_item
inventory = benchmark_2.inventory

customers = []

for i in range(10):
    customers.append(Customer())

print("your day has started\n")

time.sleep(3)

customer_number = 1

for customer in customers:
    attributes = customer.get_customer_attributes()

    ice_pref = attributes["ice_cream"]
    topping_pref = attributes["toppings"]
    price_limit = attributes["price"]

    print("Customer",customer_number)
    print("wants",ice_pref,"big handfulls of icecream")
    print("they wanted",topping_pref,"toppings")
    print("they will pay", price_limit)
    print("=========================================================")


    if (
        inventory["ice_cream"] < recipe["ice_cream"]
        or inventory["toppings"] < recipe["toppings"]
        or inventory["cones"] < recipe["cones"]
    ):
        print("Out of ingredients! Day is over.")
        break

    if (
        recipe["ice_cream"] >= ice_pref
        and recipe["toppings"] >= topping_pref
        and price_per_item <= price_limit
    ):
        print("YAYAYA your customer bought your ice cream\n")
        inventory["ice_cream"] = inventory["ice_cream"] - recipe["ice_cream"]
        inventory["toppings"] = inventory["toppings"] - recipe["toppings"]
        inventory["cones"] = inventory["cones"] - recipe["cones"]
    else:
        print("customer thought ice cream was trash\n")

    customer_number += 1

print("your day ended NOW LEAVE")
print(inventory)

