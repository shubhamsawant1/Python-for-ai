is_logged_in = False
choice = input("Are you logged in? (yes/no); ").strip().lower()


    
if choice == "yes":
    is_logged_in = True
else:
    is_logged_in = False

if is_logged_in:
    password = input("Enter your password: ")

# From comparison 
age = 18
can_vote = age >= 18 # True

score = 75
passed = score >= 60 # true

print("can_vote:", can_vote)
print("Passed:", passed)

# Comparison Operators
# These operators compare values and return True or False

age = 25

# Equality

print(age == 25)  # True  - equals 
print(age != 30)

# Greater / Less than

print(age > 20)     #True - Greater than
print(age < 30)     # True - less than
print(age >= 25)    # True - greater or equal
print(age <= 25)    # True - less or equal

# ! - Remember = assigns a value, while == compares values. This is a common source of bugs! 

