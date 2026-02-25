<<<<<<< HEAD
import benchmark_2



recipe = {
        "ice_cream": 0,
        "toppings": 0,
        "cones": 0
    }


print("\nSet your ice cream recipe!")

inventory = benchmark_2.inventory


while True:
    try:
        recipe["ice_cream"] = int(input("How many scoops of ice cream per cone? \n"))
    except:
        print("Your number was invalid, or you didn't put a number")
        print("your going to restart your recipe")
        print("")
        continue
    try:
        recipe["toppings"] = int(input("How many toppings per ice cream? \n"))

    except:
        print("your number was invalid, or you didn't put a number")
        print("your going to restart your recipe")
        print("")
        continue

    recipe["cones"] = 1

    try:
        price_per_item = float(input("How much will you sell one ice cream for? \n"))

    except:
        print("your number was invalid, or you didn't put a number")
        print("your going to restart your recipe")
        print("")
        continue
    choice = input("You finished your recipe! Will you like to make any changes? (y/n)\n")
    if choice == "y":
        print("ok")
        continue
    elif choice == "n" or choice == "":
        print("ok")
    else:
        print("ok")
    print("")
    print("You can only change your recipe during the day")
    print("")
    break


print("Recipe Completed!")
print("Current inventory:", inventory)
print("Your recipe per ice cream:", recipe)
print("Your selling price per ice cream:",price_per_item)


ice_cream_limit = inventory["ice_cream"] / recipe["ice_cream"] if recipe["ice_cream"] > 0 else 0
topping_limit = inventory["toppings"] / recipe["toppings"] if recipe["toppings"] > 0 else 0
cone_limit = inventory["cones"] / recipe["cones"] if recipe["cones"] > 0 else 0

max_cones = ice_cream_limit
if topping_limit < max_cones:
    max_cones = topping_limit
if cone_limit < max_cones:
    max_cones = cone_limit


print("Maximum number of cones you can make:", max_cones)
=======
