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