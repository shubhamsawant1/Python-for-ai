age = 25

has_license = True

# AND - both must be a true 
can_drive = age >= 16 and has_license

print(can_drive) # True

# OR - at least one  must be true

day = "Saturday"
is_weekend = day == "seturday" or day == "sunday"
print(is_weekend)

# NOT - reverse the value 

is_adult = age >= 18
is_child = not is_adult # False
print("statement",is_child)    # False

# Truth tables

# Understanding how and , not work

# AND : Both must be true

print(True and True) # true 
print(True and False) # False
print(False and False) #False

# OR: At least and must be True

print(True or False) # True
print(False or False)

# NOT: Flips the Value

print(not True)  # False
print(not False) # True