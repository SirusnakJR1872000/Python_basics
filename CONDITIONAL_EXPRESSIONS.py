# CONDITIONAL EXPRESSIONS
# Conditional Expressions are one line shortcuts for if-else statement (ternary operator)
# It will print or assign value as per the condition
# Syntax : X if condition else Y

num = int(input(" Enter a number : "))

print("Positive" if num > 0 else "Negative")

a = int(input(" Enter the first number : "))
b = int(input(" Enter the second number : "))

max = a if a > b else b
print(f" Maximum number is : {max} ")

min = a if a < b else b
print(f" Minimum number is : {min} ")
