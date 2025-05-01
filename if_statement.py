# if statement
# it basically implies that the program would do something if the condition is satisfied

age = int(input("Enter your age : "))

if age >= 18:
    print("You are eligible!")
else:
    print("You must be 18+ to sign up.")

# --------------------------------------------------------------------------------------------------------------------------

response = input("Would you like to have some food ? (Y/N) ")

if response == 'Y':
    print("You can have food.")
else:
    print("Please come again later.")

# --------------------------------------------------------------------------------------------------------------------------
name = input("Please enter your name : ")

if name == "":
    print("Please Enter your name!")
else:
    print(f"Hello {name}")

# --------------------------------------------------------------------------------------------------------------------------

# if we have a boolean value

for_sale = True

if for_sale:
    print("The item is for sale !")
else :
    print("Item is not for sale,")

# --------------------------------------------------------------------------------------------------------------------------

# Exercise - Basic Python Calculator

# The user will enter the arithmetic operator(+,-,*,/,%) and user will enter 2 numbers and we have to perform the operations based on the user's choice

import math
num_1 = float(input("Enter the first number : "))
num_2 = float(input("Enter the second number : "))

operation = input("Enter the choice of operation to be performed (+, -, *, /, %) ")

if operation == '+':
    sum = num_1 + num_2
    print(f"Sum of the 2 numbers is : {sum} ")
elif operation == '-':
    difference = num_1 - num_2
    print(f"Difference of the 2 numbers is : {difference}")
elif operation == '*':
    product = num_1 * num_2
    print(f"Product of the  numbers is : {product}")
elif operation == '/':
    quotient = num_1 / num_2
    print(f"Quotient of the numbers is : {quotient}")
elif operation == '%':
    remainder = num_1 % num_2
    print(f"Remainder of the 2 numbers is : {remainder}")
else:
    print("Please enter a valid operator!")