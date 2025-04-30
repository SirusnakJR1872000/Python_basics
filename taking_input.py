# input() is a function that prompts the user to enter the data and return the data in the form of strings

name = input("What is your name ? ")

# age += 1

# Traceback (most recent call last):
# File "/Users/gauravpatil/Desktop/Gaurav/advanced_algorithm_cpp/python basics/taking_input.py", line 5, in <module>
# age += 1
# TypeError: can only concatenate str (not "int") to str

# Since the input() gives the output in the form of strings we cannot perform arithmetic operations
# So we can overcome this by type casting
# Here we will convert string to int

age = int(input("What is your age ? "))
age += 1
print(f"Hello {name}!")
print(f"You are {age} years old ")

# Exercise 1 : Find out the area of rectangle and ask the user to enter the values of length and breadth

length = int(input("Enter the length of the rectangle : "))
breadth = int(input("Enter the breadth of the rectangle : "))

area = length * breadth
print(f"Area of rectangle is {area} sq. units")

# Exercise 2 : Shopping Cart 
item = input("What item are you looking to buy ? ")
price = float(input(f"What is the price of the {item} : "))
quantity = int(input("How much do you need ? "))

total = price * quantity
print(f"Your total is ${total}")
