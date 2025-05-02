# while loop : executes the statement until the condition is true 
# it is important to note that we need to specify a exit statement
# otherwise our code would be stuck in a infinite loop

# lets say we ask the user to enter a number between 1 - 10 and if the input is anything except the range between 1 - 10 then we exit

# take the input from the user
num = int(input(" Enter a number between 1 - 10 : "))

# mention the while condition that the number cannot be less than 1 and greater than 10
while num < 1 or num > 10:
    print(f"{num} is not valid ! ")
    num = int(input("Please Enter a value between 1 - 10 ! "))

print(f"Your number is : {num}")