#randomisation and lists

"""
import random

# random.randint generates ints btwn >=1 and <=10
random_int  = random.randint(1,10)
print(random_int)

# random.random generates number btwn >=0 and <=1
random_number = random.random()*10
print(random_number)

# random.uniform generates number from >=1 to <=10
random_float = random.uniform(1,10)
print(random_float)

random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")


# lists
fruits = ["cherry","apple","banana","strawberry","kiwi","mango","peach"]
print(fruits[2])
print(fruits[-3])

fruits.append("pine apple")
print(fruits)
fruits[-1] = "pineapple"
fruits.extend(["berry","melon"])
print(fruits)

# Randomise Bill Payment
friends = ["Alice","Bob","Charlie","David","Emanuel"]
who_pays = random.randint(0,len(friends)-1)
print(f"{friends[who_pays]} will pay the bill")

who_pays = random.choice(friends)
print(f"{who_pays} will pay the bill")
"""

# Rock Paper Scissors Lizard Spock Game with Computer
# Rules - https://global.discourse-cdn.com/codecademy/original/5X/1/e/9/a/1e9ae22826a47a2d2e9f0e8f0f0cdf21a8479715.jpeg

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
    ________
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Lizard
lizard = """
---.___________
        _______)
---.________)
"""

# Spock
spock = """
    ⌠⌒|
 ⌠⌒⌉| |   ◜﹆◜﹆
 | ||⩧|  / // /
 |_|| | /-//=/
 | || |/ // /
 ( || | // /
 |         .______
 |         __⫫____)
  |       |
"""

print("\nWelcome to Rock 🪨, Paper 📄, Scissors , Lizard 🦎, Spock 🖖🏽\n\nWe will play 3 rounds and then decide the winner")

game = 1
user_wins = 0
comp_wins = 0
options = ['scissors','paper','rock','lizard','spock']
options_art = [scissors,paper,rock,lizard,spock]

while game <=3:
    user = input(f"\nRound {game}\nPick your move - Rock, Paper, Scissors, Lizard or Spock?   ").lower()
    comp_choice = random.randint(0,len(options)-1)
    comp = options[comp_choice]
    if user in options:
        print(f"Your move: {options_art[options.index(user)]} {user}\n\nComputer's move: {options_art[options.index(comp)]} {comp}\n")
        game += 1
        if options.index(user) + 1 == options.index(comp):
            user_wins += 1
            print("You win!")    
        elif options.index(user) == options.index(comp) + 2:
            user_wins += 1
            print("You win!")    
        elif options.index(user) == options.index(comp):
            print("It's a tie")
        else:
            comp_wins += 1
            print("Computer wins :(")
    else:
        print("Invalid choice!")

print(f"\n\n********** RESULT ***********\nYour score: {user_wins}\tComputer's score: {comp_wins}\n")
if user_wins > comp_wins:
    print("You beat the Computer!!!\n\n")
elif user_wins == comp_wins:
    print("Its a tie, run code to try again\n\n")
else:
    print("Computer wins. Better luck next time!\n\n")
