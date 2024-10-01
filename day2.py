#learnt data types and string manipulation
"""
print("Hello"[3])

print("123" + "123")
print(123 + 123)

value = 123900070
print(f'{value:,}')
"""

print("\nWelcome to the Tip Calculator 🥗💲\n")

amount = float(input("What is the final bill amount? $"))
tip_percent = float(input("How much % tip would you like to give? 0,10,15 or 20? "))/100

tip = tip_percent * amount

num = int(input("How many people to split the bill between? "))

each = round((amount + tip)/num,2)

print("\nEach person should pay -  $" + str(each))
