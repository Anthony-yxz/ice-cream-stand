import benchmark_2



recipe = {
        "ice_cream": 0,
        "toppings": 0,
        "cones": 0
    }


print("\nSet your ice cream recipe!")

inventory = benchmark_2.inventory
try:
    recipe["ice_cream"] = int(input("How many scoops of ice cream per cone? \n"))
except:
    print("your number was invalid")

try:
    recipe["toppings"] = int(input("How many toppings per ice cream? \n"))
except:
    print("your number was invalid")

recipe["cones"] = 1

try:
    price_per_item = float(input("How much will you sell one cone for? \n"))
except:
    print("your number was invalid")


print("\nCurrent inventory:", inventory)
print("Your recipe per cone:", recipe)
print("Your selling price per cone:", price_per_item)


ice_cream_limit = inventory["ice_cream"] / recipe["ice_cream"] if recipe["ice_cream"] > 0 else 0
topping_limit = inventory["toppings"] / recipe["toppings"] if recipe["toppings"] > 0 else 0
cone_limit = inventory["cones"] / recipe["cones"] if recipe["cones"] > 0 else 0


max_cones = ice_cream_limit
if topping_limit < max_cones:
    max_cones = topping_limit
if cone_limit < max_cones:
    max_cones = cone_limit


print("Maximum number of cones you can make:", max_cones)




