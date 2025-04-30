# Minutes to Hours and Minutes

# Here we will convert a number which is given in minutes to hours and minutes format

total_time = int(input(" Enter the minutes which are to be converted in hours and minutes format : "))

hours = total_time // 60

minutes = total_time % 60

print(f" The time {total_time} in hours and minutes format is {hours} hours and {minutes} minutes ")