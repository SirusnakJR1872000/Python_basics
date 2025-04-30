# BMI calculator

# we will ask the user their weight in kg and height in meters, then calculate and print the BMI

# BMI = weight/sq(height)

import math

weight = float(input("Enter your weight in kg. : "))
height = float(input("Enter your height in meters : "))

BMI = weight / math.pow(height, 2)

print(f"Your BMI is : {round(BMI,2)}")



