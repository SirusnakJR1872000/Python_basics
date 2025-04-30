# Here are going to have a look at the variables 
# Variables are nothing but a container for a particular value
# There are mainly 4 types of variables namely string, integer, float, boolean 
# Each variable in the code must have a unique name
# To assign a variable with a value we use the assignment "=" operator

# Lets start with the first type of variables which are the strings

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# Strings are nothing but the sequence of characters
# So when we define a variable with a string we have to enclose it within the double quotes or single quotes

first_name = "SirusnakJr"

# if we are adding double quotes in the print statement itself then we will print the exact same thing which is within the quotes
print("first_name")
# So here we have a variable defined as first_name but since the variable is given in the double quotes in the print statement it is going to treat it as 
# a string rather than a variable 

# Hence the correct approach is to not use double quotes if you want to print the value of the variable 
print(first_name)

# But if at all you want to use the quotes in the print statement along with some text then you use the 'FORMAT' operator 'f'
print(f"Hello Everyone. My name is {first_name}")
# Here we will use the format operator along with the place holder {} 
# Syntax : print(f"statement {place holder}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Now we will move forward with the Integers
# Integers are nothing but the whole numbers 
# Unlike the Strings, we don't have to mention the Integers within the double quotes otherwise it would be regarded as a string

age = 24
num_of_students = 50
print(age)

# again if you want to add some text along with the variable we can use the format operator
print(f"My age is {age}")
print(f"My class has {num_of_students} students")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Moving on the next type which is the float value 
# Float or the Floating point Numbers are the integer values followed by a decimal point and numbers after that such as 10.99

price = 999.99
gpa = 3.67
distance = 6.9

print(f"Price of the iPhone is ${price}")
print(f"My GPA was {gpa}")
print(f"I ran {distance}km.")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# Next is the boolean value 
# A boolean value is either True or False and is not output directly unlike the previous types
# It is meant to be programmed internally within the code
# In simple words it can be used to check a condition and display the value as per the condition

is_student = False

if is_student:
    print(f"{first_name} is a student")
else:
    print(f"{first_name} is NOT a student")