# To check if the numbers are even or odd we will divide them by 2 
# So if the remainder is 0 then we know that the number is even otherwise odd

num = int(input(" Enter the value of the number to check if it even or odd : "))

if num % 2 == 0 :
    print(f" {num} is even")
else:
    print(f" {num} is odd")