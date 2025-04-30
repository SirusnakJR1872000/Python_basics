# Here we have to swap 2 numbers 
# take 2 numbers as the input and swap them and display the numbers after swapping

num_1 = int(input("Enter the value of the first number : "))
num_2 = int(input("Enter the value of the second number : "))

# now lets take a temporary variable where we will store the value
temp = num_1
num_1 = num_2
num_2 = temp

print(f"Values of the numbers after swapping are num_1 : {num_1} and num_2 : {num_2}")