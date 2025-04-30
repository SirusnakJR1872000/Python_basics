# Sum of Digits
# Here we are going to take a number and find the sum of the digits

# Lets take the input number
num = int(input("Enter the number whose sum is to be calculated : "))

digit_sum = 0

while num > 0:
    # get the last digit
    last_digit = num % 10
    # add it to the sum of the digits
    digit_sum += last_digit
    # now remove the last digit
    num //= 10 # // is the floor division operator where it would remove the decimal part of the number eg. 439 // 10 = 43 instead of 43.9 

print(f"Sum of the digits of the number {num} is : {digit_sum}")
