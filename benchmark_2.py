money = 25.0

inventory = {
    "ice_cream": 0,
    "cones": 0,
    "toppings": 0
}

prices = {
    "ice_cream": 2.0,
    "cones": 1.0,
    "toppings": 1.50
}

print("Welcome to my ice cream stand")

while True:
    print("Money:", money)
    print("Inventory:", inventory)

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
        print("your number was invalid please try again")
        continue

    if amount <= 0:
        print("You must buy at least 1 item or exit the shop")
        continue

    if choice == "1":
        cost = amount * prices["ice_cream"]
        if cost <= money:
            money = money - cost
            inventory["ice_cream"] = inventory["ice_cream"] + amount
            print("you bough ice creams")
        else:
            print("Not enough money")

    elif choice == "2":
        cost = amount * prices["cones"]
        if cost <= money:
            money = money - cost
            inventory["cones"] = inventory["cones"] + amount
            print("you bough cones")
        else:
            print("Not enough money")

    elif choice == "3":
        cost = amount * prices["toppings"]
        if cost <= money:
            money = money - cost
            inventory["toppings"] = inventory["toppings"] + amount
            print("you bough toppings")
        else:
            print("Not enough money")

    else:
        print("Invalid choice")