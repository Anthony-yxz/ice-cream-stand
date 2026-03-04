import time
import bench234info

def run_shop():

    inventory = bench234info.inventory
    money = bench234info.money

    prices = {
        "ice_cream": 2.0,
        "cones": 1.0,
        "toppings": 1.50
    }

    print("Welcome to the shop")

    while True:
        print("Money:",bench234info.money)
        print("Inventory:", bench234info.inventory)

        print("What would you like to buy")
        print("1 ice cream is 2.00 dollar each")
        print("2 the cones are 1.00 dollar each")
        print("3 the toppings are a 1.50 each")
        print("4 Exit")

        choice = input("Enter choice: ")

        if choice == "4":
            print("you chose to exit the shop")
            break

        amount = input("How many do you want to buy ")

        if amount.isdigit():
            amount = int(amount)
        else:
            print("======INVALID======")
            time.sleep(2)
            continue

        if amount <= 0:
            print("You can either shop for items, or exit the shop")
            time.sleep(2)
            continue

        if choice == "1":
            cost = amount * prices["ice_cream"]
            if cost <= bench234info.money:
                bench234info.money -= cost
                bench234info.inventory["ice_cream"] += amount
                print("you bought ice creams")
            else:
                print("======TO BROKE======")
                time.sleep(2)

        elif choice == "2":
            cost = amount * prices["cones"]
            if cost <= bench234info.money:
                bench234info.money -= cost
                bench234info.inventory["cones"] += amount
                print("you bought cones")
            else:
                print("======TO BROKE======")
                time.sleep(2)

        elif choice == "3":
            cost = amount * prices["toppings"]
            if cost <= bench234info.money:
                bench234info.money -= cost
                bench234info.inventory["toppings"] += amount
                print("you bought toppings")
            else:
                print("======TO BROKE======")
                time.sleep(2)

        else:
            print("Invalid choice")
            time.sleep(2)
