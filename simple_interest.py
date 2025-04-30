# Here we will calculate the simple interest which is given by the formula
# I = (P*r*n)/100

p = float(input(" Enter the principal amount : "))
r = float(input(" Enter the rate of the interest : "))
n = int(input(" Enter the number of years : "))

interest = (p * r * n)/100

print(f"The interest for the {p} amount at {r}% rate is : {round(interest, 2)} ")