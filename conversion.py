# Convert Seconds to Hours, Minutes, and Seconds
# Take total seconds as input and convert them into hours, minutes, and seconds.
# Example: 3665 → 1 hour, 1 minute, 5 seconds

# total_seconds = int(input("Enter the total seconds : "))

# hours = total_seconds // 3600
#remianing_seconds = total_seconds % 3600
#minutes = remianing_seconds // 60
#seconds = remianing_seconds % 60

#print(f"Conversion of {total_seconds} into hours, minutes and seconds format : {hours} hour, {minutes} minutes, {seconds} seconds")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# Age in Days, Months, and Years
# Take your age in years and calculate the approximate number of days and months you've lived.
# (Assume 1 year = 12 months, 1 year ≈ 365 days)

age = int(input("Enter your age in years : "))

months = age * 12
days = age * 365

print(f"You have lived for {months} months or {days} days")

