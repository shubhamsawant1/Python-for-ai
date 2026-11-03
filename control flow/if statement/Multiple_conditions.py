# Multiple Conditions
# Combine condition with and , or , not

age = 25

has_license = True

# Both must be True

if age >= 18 and has_license:
   print("You can drive!") 

def check_day(day):
    if day == "Saturday" or day == "Sunday":
        return True
    else:
        return False

# At least one must be True
today = input("Enter the day of the week: ").title().strip()
if check_day(today):
    print("You can relax!")
else:
    print("You have to work!")

