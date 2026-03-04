import time
import STORY_LINE
import benchmark_2
import benchmark_3
import benchmark_4
import bench234info

benchmark_2.run_shop()
benchmark_3.set_recipe()

print("\n"*3)

while True:

    if bench234info.money <= 0:
        print("You ran out of money bro but ill spare you a 50\n","but can you please pay me back later")
        time.sleep(1.5)
        bench234info.money =+ 50
    if bench234info.day > 7:
        print("Congratulations on surviving 7 full days, it might have been the easiest game in the world,\n","but its the effort that counts, lebron soon went on to give you 5 million dollars like he prommised")
        print("+5 million dollars from lebron")
        time.sleep(1.5)
        break   

    print("\n" * 2)
    print("day",bench234info.day)
    print("Thank you for setting up your stand!")
    print("What would you like to do from here?")
    time.sleep(1.5)
    print("\n" * 2)
    print("1  Go back to shop")
    print("2  Change your recipe")
    print("3  START DAY")
    print("4  learn how to play")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        benchmark_2.run_shop()

    elif choice == "2":
        benchmark_3.set_recipe()
        

    elif choice == "3":
        benchmark_4.run_day()
        bench234info.day += 1

        
    elif choice == "4":
        print("this is your ice cream standn\n","your goal is to survive 7 days without running out of money\n","you can buy from the shop,change your recipe,or start your day\n")
        time.sleep(1.5)
    else:
        print("atleast play the game right, enter 1, 2, 3, or 4 or click ctrl+C")
        time.sleep(1)
