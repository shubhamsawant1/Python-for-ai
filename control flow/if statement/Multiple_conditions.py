# Multiple Conditions
# Combine condition with and , or , not

age = 25

has_license = True

# Both must be True

if age >= 18 and has_license:
   print("You can drive!") 

# At least one must be True
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


# Reverse the condition with not

def is_raining(raining):
    if raining == "No":
        return not True
    else:
        return True

raining = input("It is raining? (yes/no): ").title().strip()

if is_raining(raining):
    print("Take an umbrella!")
else:
    print("No need for an Umbrella!")




