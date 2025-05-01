# Indexing 
# idexing is the process of accessing elements of a sequence using [] which is the indexing operator
# [start : end : step]
# here the start is inclusive and end is exclusive 
# so for example if you want to access the first 4 element then you would write [0:4] because 4 is exclusive
# you can also omit the 0 which is the start, here if nothing is mentioned then python assumes that we want to print from the start till the end - 1 element [:4]
# similarly if you need to print from a particular index to the end then you dont have to specify the end parameter, python will assume it to be the end
# you can also access the end element by mentioning the end parameter as -1 and so on for reverse fashion, negative basically refers to the reverse accessibility of the elements

credit_number = '2079-5776-2067-1079'

# accessing first element
# print(credit_number[0])

# accessing the third element
# print(credit_number[4])

# accessing the elements from 5 to 8 
# print(credit_number[5:9])

# accessing the elements from 5th position to the end
# print(credit_number[5:])

# getting the last element 
# print(credit_number[-1])

# if we want to get every 3rd number
# print(credit_number[::3])

# get the last 4 digits of the credit card 

last_digit = credit_number[-4:]

print(f" Your credit card number is : XXXX-XXXX-XXXX-{last_digit} ")

