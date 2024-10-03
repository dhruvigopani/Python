#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to The Python Password Generator\n\n")
letter_input = int(input("How many letters would you like in your password?  "))
number_input = int(input("How many numbers would you like in your password?  "))
symbol_input = int(input("How many symbols woudl you like in your password?  "))

#pattern - letters followed by numbers followed by symbols
password = ""
for i in range(0,letter_input):
    password += random.choice(letters)
for j in range(0,number_input):
    password += random.choice(numbers)
for k in range(0,symbol_input):
    password += random.choice(symbols)
print(f"\nYour Patterned Password can be    {password}")

#no pattern
password = ""
password_list = []
for i in range(0,letter_input):
    password_list.append(random.choice(letters))
for j in range(0,number_input):
    password_list.append(random.choice(numbers))
for k in range(0,symbol_input):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

for value in password_list:
    password += value
print(f"\nYour High-Level Password can be    {password}\n")
