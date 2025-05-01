# Even or Odd Identifier
# Write a program that takes an integer input and prints "Even" if it's even, otherwise "Odd" using a conditional expression.

number = int(input(" Enter a number : "))

print("Even" if number % 2 == 0 else "Odd")

#----------------------------------------------------------------------------------------------------------------------------------------------------

# String Contains Check
# Ask the user to input a sentence. Check if it contains the word "Python" using a logical operator.

sentence = input(" Enter a sentence : ")

if 'Python' in sentence:
    print(" Python is in the sentence ")
else:
    print(" Python is not in the sentence ")

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Extract Initials
# Given a full name (e.g., "John Doe"), extract and print the initials using string indexing.

name = input(" Enter your full name : ")

first, last = name.split()

initials = first[0].upper() + last[0].upper()

print(f" Your initials are : {initials}")

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Problem: Last Letter Collector
# Ask the user to input their full name (e.g., "John Doe"), and print the last letter of each name part (e.g., "ne").

name = input(" Enter your name : ")

first, last = name.split()

last_letter = first[-1] + last[-1]

print(f"Last letters are : {last_letter}")

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Problem: Middle Letter Extractor
# Ask the user to enter a single word.
# If the word has an odd number of letters, print the middle letter.
# If it has an even number, print the two middle letters.

word = input(" Please enter a single word : ")

count = len(word)
n = len(word) // 2

if count % 2 == 0:
    print(word[n-1:n+1])
else:
    print(word[n])

#----------------------------------------------------------------------------------------------------------------------------------------------------

# Temperature Check
# Take input for a temperature in Celsius. Print "Hot" if it's more than 30, "Warm" if between 20 and 30, else "Cold". Use chained conditional expressions (if...elif...else).

temp = int(input("Please enter a temperature in degree celcius: "))

if temp > 30:
    print(" hot ")
elif 20 < temp < 30:
    print(" Warm ")
else:
    print(" Cold ")

#----------------------------------------------------------------------------------------------------------------------------------------------------

# Username Validator
# Ask the user for a username and:

# Ensure it's at least 5 characters long

# Doesn’t start with a number
# Print "Valid" or "Invalid" using string indexing and logical operators.

username = input(" Enter your username : ")

length = len(username)

if length > 5 or username[0].isdigit():
    print(" Invalid ")
else:
    print(" Valid ")

#----------------------------------------------------------------------------------------------------------------------------------------------------

# Format a Bill
#Take input for item, quantity, and price. Print a formatted bill using format specifiers like:

#Item     Quantity    Price
#Apple    2           $1.50

item = input(" Please enter an item : ")
quantity = input(" Please enter the quantity : ")
price = float(input(" Please enter the price : "))

print(f"{'Item':<10} {'Quantity':<10} {'Price':<10}")
print(f"{item:<10} {quantity:<10} {'$' + format(price, '.2f'):<10}")

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Problem: Shopping Receipt Generator
# Ask the user to enter three items, along with their quantities and prices. Then print a neat receipt showing all the data in tabular form, including the total cost.

# ✅ Input:
# Ask for:

# Item name

# Quantity

# Price per unit
# → Do this 3 times

# ✅ Example Output:

# Item       Quantity  Price     Total     
# Apple      2         $1.50     $3.00     
# Milk       1         $2.25     $2.25     
# Bread      3         $1.00     $3.00     

# Grand Total: $8.25

# first we will create a empty list to store items

items = []

# now we will need to run the loop 3 times

for _ in range(3):
    item = input(" Please enter an item : ")
    quantity = int(input(" Please enter the quantity : "))
    price = float(input(" Please enter the price : "))
    total = quantity * price
    # now we will add everything to the items list
    items.append((item, quantity, price, total))

# lets print the header
print(f"{'Item':<10} {'Quantity':<10} {'Price':<10} {'Total':<10}")

# initialize the grand total to 0
grand_total = 0 

# now we will print from the items list
for item, quantity, price, total in items:
    print(f"{item:<10} {quantity:<10} {'$' + format(price, '.2f'):<10} {'$' + format(total, '.2f'):<10}")

    # calculate the grand total
    grand_total += total 

# now print it
print(f"Grand Total : {'$' + format(grand_total,'.2f')}")

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Palindrome Checker (Case-insensitive)
# Check if a string is a palindrome (same forward and backward), ignoring case and spaces.

name = input(" Enter the string : ")


if name == name[::-1]:
    print(f" The string {name} is a Palindrome ")
else:
    print(f" The string {name} is not a Palindrome ")


    


