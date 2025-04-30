# So starting with the basic arithmetic fucntions such as addition, subtraction, multiplication, division, exponent
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Addition
num = 5
# num = num + 3
# this is the basic arithmetic addition function

num += 3
# this is the augmented operator as it requires less code
print(num)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Subtraction
# num = num - 2
num -= 2
print(num)

# Multiplication
# num = num * 2
num *= 2
print(num)

# Divison
# num = num / 4
num /= 4
print(num)

# Exponent
# num = num ** 2
num **= 2
print(num)

# Modulus
# mod = mod % 3
num %= 3
print(num)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Some basic function such as the round off, absolute value, power, min and max functions

x = 4.67
y = -5
z = 7

roff = round(x)
print(roff)

abs_val = abs(y)
print(abs_val)

exp_val = pow(z, 3)
print(exp_val)

print(min(x, y, z))

print(max(x, y, z))

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Some basic function using the math library
import math

a = 10.34

# to get the value of pi
print(math.pi)

# to get the value of exponential constant
print(math.e)

# to find the square root of the number
sqroot = math.sqrt(100)
print(sqroot)

# to find the ceiling that is to round up 
roundup = math.ceil(a)
print(roundup)

# to find the floor that is to round down
rounddown = math.floor(a)
print(rounddown)

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Exercise : To find the circumference of the circle

# formula : C = 2 * pi * r

import math

radius = int(input("Enter the radius of the circle : "))

circumference = 2 * math.pi * radius
print(f"Circumference of the circle is : {round(circumference, 2)} units")

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Exercise : To find the Area of the circle

# formula : A = pi * r * r

import math

area = math.pi * pow(radius, 2)
print(f"Area of the circle is {round(area, 3)}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Exercise to find the hypotenuse of the right angled triangle

# formula : h = sqrt[sq(side1) + sq(side2)]

import math

side_1 = int(input("Enter the length of the first side of the triangle : "))
side_2 = int(input("Enter the length of the second side of the triangle : "))

hypotenuse = math.sqrt(math.pow(side_1, 2) + math.pow(side_2, 2))
print(f"Hypotenuse of the triangle is : {round(hypotenuse, 2)} units")