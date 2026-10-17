is_logged_in = False
choice = input("Are you logged in? (yes/no); ").strip().lower()


    
if choice == "yes":
    is_logged_in = True
else:
    is_logged_in = False

if is_logged_in:
    password = input("Enter your password: ")

