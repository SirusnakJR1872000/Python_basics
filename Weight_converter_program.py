# Weight converter program
# Take the weight input from the user and ask the user if it is in kgs or lbs and convert it into other weight standards (kgs to lbs or lbs to kgs) 
# and also display the result

weight = float(input(" Please enter your weight : "))
unit = (input(" Mention the unit of weight kgs(k) or lbs(L): "))

if unit == 'K':
    weight = weight * 2.205
    unit = 'Lbs'
    print(f" Your weight is : {round(weight, 2)} {unit}")
elif unit == 'L':
    weight = weight / 2.205
    unit = 'Kgs'
    print(f" Your weight is : {round(weight, 2)} {unit}")
else :
    print(f"{unit} was not valid. Please Enter a choice between K or L")

