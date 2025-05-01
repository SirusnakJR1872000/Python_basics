# Logical Operators
# Logical operators are used to evaluate multiple conditions
# We have 3 basic operators : and, or, not
# or : atleast one condition must be true to execute the statement
# and : both conditions have to be true to execute the statement
# not : inverts the condition (not False, not True)

# -------------------------------------------------------------------------------------------------------------------------------------------------
# OR Operator 
# -------------------------------------------------------------------------------------------------------------------------------------------------

temp = int(input("Enter the temperature : "))
#is_raining = False

#if temp > 35 or temp < 0 or is_raining:
#    print("Not suitable weather")
#elif 0 <= temp <= 35 or is_raining:
#    print("You have a good day")
#else:
#    print("Stay at home!")

# -------------------------------------------------------------------------------------------------------------------------------------------------
# AND Operator
# -------------------------------------------------------------------------------------------------------------------------------------------------

#is_sunny = True

#if temp > 35 and is_sunny:
#    print("It is hot outside !")
#elif 0 < temp <= 35 and is_sunny:
#    print("It is a good weather !")
#else:
#    print("Stay at home! ")

# -------------------------------------------------------------------------------------------------------------------------------------------------
# NOT Operator
# -------------------------------------------------------------------------------------------------------------------------------------------------

is_rain = False
if temp > 35 and not is_rain:
    print("It is warm")
elif 0 < temp <= 35 and not is_rain:
    print("It is a good weather")
else:
    print("Stay at home")

# -------------------------------------------------------------------------------------------------------------------------------------------------
