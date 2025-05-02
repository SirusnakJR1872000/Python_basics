# for loops
# we use for loops to iterate over a particular range
#unlike the while loop which can go uptil infinite times
# here we specify the lower range and the upper range and wwe can also specify the steps 

# Sytax : for i in range(lower range, upper range, steps)
# here the upper range is always exclusive and lower range is inclusive so while specifying the upper range make sure to mention one plus of the upper range 
# to get the reverse just use reversed()

# suppose we want to print values from 1 - 20

for _ in range(1, 21):
    print(_)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# now if we want to print the numbers in reverse order

for _ in reversed(range(1,21)):
    print(_)

# another technique is by using step 

for _ in range(20, 0, -1):
    print(_)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# lets say we want to print every second or third value

for _ in range(1, 21, 2):
    print(_)

for _ in range(1, 21, 3):
    print(_)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# suppose we want to print the numbers of the credit card
credit_number = '2079-5778-1607-2779'

for _ in credit_number:
    print(_)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# suppose we don't want to print a particular number in the range

for _ in range(1, 21):
    if _ == 13:
     continue
else:
    print(_)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# suppose we want to stop printing at a particular number

for i in range(1, 21):
    if i == 13:
        break
    else:
        print(i)