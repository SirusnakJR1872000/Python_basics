# Calculate Final Price with Discount
# Ask the user for the original price of an item and a discount percentage. Print the final price after applying the discount.

price = int(input(" Enter the original price of the item : "))
discount = float(input(" Enter the discount percentage of the item : "))

discount_amount = price * discount/100

Final_price = price - discount_amount

print(f"Final price of the product after the dicount is : {Final_price}")