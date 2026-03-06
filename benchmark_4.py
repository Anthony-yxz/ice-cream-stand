import time
import bench234info
from customer_class import Customer


def run_day():
    recipe = bench234info.recipe
    price_per_item = bench234info.price_per_item
    inventory = bench234info.inventory

    customers = []

    for i in range(20):
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
            bench234info.money = bench234info.money + price_per_item
            inventory["ice_cream"] = inventory["ice_cream"] - recipe["ice_cream"]
            inventory["toppings"] = inventory["toppings"] - recipe["toppings"]
            inventory["cones"] = inventory["cones"] - recipe["cones"]
        else:
            print("customer thought ice cream was trash\n")

        customer_number += 1

    print("your day ended NOW LEAVE")

