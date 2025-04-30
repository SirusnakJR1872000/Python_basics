# Type Casting is the method of converting one data type to another data type eg: string -> integer, integer -> float and so on
# str(), int(), float(), bool() are the methods used to convert

name = 'SirusnakJr'
age = 24
gpa = 3.67
is_student = True

# Lets first check the data types of the variables
# we can do that by using type()

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# Now lets conver the floating point value to a integer value 
gpa = int(gpa)
print(gpa)
print(type(gpa))

age = float(age)
print(age)
print(type(age))

# It is important to note that strings and numbers cannot be concatenated or be used arithmatically together
# age = str(age)
# age += 1
# print(age)
# TypeError: can only concatenate str (not "int") to str 

age_1 = 25
age_1 = str(age_1)
age_1 += '1'
print(age_1)

# since we are adding both string the '1' gets concatenated to the end rather than adding up in the value

# by using boolean type casting we can check if the value entered is true or not
last_name = 'JR'
last_name = bool(last_name)
print(type(last_name))

print(last_name)

last_name_1 = ''
last_name_1 = bool(last_name_1)
print(type(last_name_1))

print(last_name_1)

