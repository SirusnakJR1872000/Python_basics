# STRING OPERATIONS

username = input(" Enter your username : ")
phone_number = (input(" Enter your phone number : "))

# -------------------------------------------------------------------------------------------------------------------------------------------------
# len() : used to find the length of the string
# -------------------------------------------------------------------------------------------------------------------------------------------------

# result = len(name) # used to find the length of the string 
# if spaces are present within the string then they are also taken into consideration

# -------------------------------------------------------------------------------------------------------------------------------------------------
# find() : used to find the first occurance of any character in the string
# -------------------------------------------------------------------------------------------------------------------------------------------------

# result = name.find('a') always the first occurance is taken into consideration and not every charcter

# result = name.rfind('a') # helps us to find the occurance of a particular character from the end i.e. reverse order hence the name rfind

# -------------------------------------------------------------------------------------------------------------------------------------------------
# capitalize() : helps us to capitalize the first letter of the string
# -------------------------------------------------------------------------------------------------------------------------------------------------

# result = name.capitalize() 

# -------------------------------------------------------------------------------------------------------------------------------------------------
# upper() : helps us to capitalize all the characters of the string
# -------------------------------------------------------------------------------------------------------------------------------------------------

# result = name.upper()

# -------------------------------------------------------------------------------------------------------------------------------------------------
# lower() : helps us to convert all upper case characters to lower case characters
# -------------------------------------------------------------------------------------------------------------------------------------------------

# result = name.lower()

# -------------------------------------------------------------------------------------------------------------------------------------------------
# isdigit() : helps us to check if the given string is entirely digits or not
# -------------------------------------------------------------------------------------------------------------------------------------------------

# result = name.isdigit()

# -------------------------------------------------------------------------------------------------------------------------------------------------
# isalpha() : used to check if the given string is entirely alphabets or not; even spaces are not counted and we would get False eg: Gaurav Patil
# -------------------------------------------------------------------------------------------------------------------------------------------------

#result = name.isalpha()

# -------------------------------------------------------------------------------------------------------------------------------------------------
# count() : used to find the occurances of a praticular character within the string
# -------------------------------------------------------------------------------------------------------------------------------------------------

# result = phone_number.count('-')

# -------------------------------------------------------------------------------------------------------------------------------------------------
# replace() : used to replace a particular value of a string with another value
# -------------------------------------------------------------------------------------------------------------------------------------------------

# result = phone_number.replace('-','/')

# print(result)

# -------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise : Validate user input
#            username must not have more than 12 characters
#            username must not contain spaces
#            username must not contain digits
# -------------------------------------------------------------------------------------------------------------------------------------------------


if len(username) > 12:
    print(" Username cannot exceed more than 12 characters. ")
elif not username.find(' ') ==  -1:
    print("Username should not contain spaces.")
elif not username.isalpha():
    print(" Username cannot conatin digits")
else:
    print(f" Welcome {username} ")

