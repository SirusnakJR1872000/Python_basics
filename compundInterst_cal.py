# Here we will design a compound interest calculator
# we need to make sure that the values of Principal amount, time and rate of interest cannot be equal to or less than zero

# initially lets assign a default value of 0 to these paramteres and ask for the new value to be entered

import math 

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input(" Enter the principal amount : "))
    if principal <= 0:
        print(" Principal amount cannot be less than or equal to 0! ")


while rate <= 0:
    rate = float(input(" Enter the rate of interest : "))
    if rate <= 0:
        print(" Rate cannot be less than or equal to 0! ")

while time <= 0:
    time = int(input(" Enter the period in years : "))
    if time <= 0:
        print(" Time cannot be negative! ")


# now we will calculate the amount 

total_amount = round(principal * math.pow((1 + (rate/100)), time), 2)

# now we will print the amount

print(f" The amount to be given at the interest of {rate}% in {time} years is : ${total_amount}  ")