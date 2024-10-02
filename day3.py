#learning if/else conditional statements and modulo operator
"""
print("\n🎡 Welcome to the Rollercoaster! 🎢 \n")
height = float(input("What is your height in cm? "))
age = int(input("What is your age? "))
ticket = 0
total_fare = 0
if height > 120:
    print("Wohooo!! You can ride the rollercoaster!")
    pictures = input("Do you want pictures? Type Yes or No  - ").lower()
    if age <= 12:
        ticket = 5
        print("Child ticket fare is $5")
    elif 12 < age <= 18:
        ticket = 7
        print("Youth ticket fare is $7")
    elif age >= 45 and age <= 55:
        print("Ride is free for you! Enjoy!!")
    else:
        ticket = 12
        print("Adult ticket fare is $12")

    if pictures == 'yes':
        total_fare = ticket + 3
        print(f"Your total fare is ${total_fare}\n")
    elif pictures == 'no':
        print(f"Your total fare is ${total_fare}\n")
    else:
        print("Invalid input\n")

else:
    print("Sorry, you can't ride the rollercoaster :(\n")

"""

"""
num = int(input("What is the number you want to check?" ))
if num%2==0:
    print("Its an even number!")
else:
    print("Its odd")
"""
"""
print("\n🍕 Welcome to Python Pizza Delivery 🍕\n")
size = input("What size pizza do you want? S, M or L  - ").lower()

pizza_cost = 0
if size == 's':
    pizza_cost = 15
elif size == 'm':
    pizza_cost = 20
elif size == 'l':
    pizza_cost = 25
else:
    print("Invalid input")

pepperoni = input("Do you wnat pepperoni on the pizza? Yes or No  - ").lower()
if pepperoni == 'yes':
    if size == 's':
        pizza_cost += 2
    elif size == 'm' or size == 'l':
            pizza_cost += 3

extra_cheese = input("Do you wnat extra cheese on your pizza? Yes or no  - ").lower()
if extra_cheese == 'yes':
    pizza_cost += 1

print(f"Your total bill is ${pizza_cost}")
"""

#ascii art assigned to variable as a triple quote raw string since it contains escape characters

treasure = r"""
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
"""
print(treasure)
print("\nWelcome to the Treasure Island 🏝️🏴‍☠️\nYour mission is to find the treasure\n")

direction = input("You're at a crossroad. Where do you want to go? Left or Right?   ").lower()
if direction == 'left':
    swimming = input("You've come to the lake. There is an island in the lake. Do you want to swim across or wait for a boat? Type swim or wait.   ").lower()
    if swimming == 'wait':
        door = input("You've arrived at the island. The house has 3 doors, pick one. Red, Yellow or Blue?   ").lower()
        if door == 'yellow':
            print("Congratulations! You Win!! 🎉")
        else:
            print("Game Over!💀")
    else:
            print("You were attacked by an alligator. Game Over!💀")
else:
    print("You fell into a hole. Game Over!💀")
