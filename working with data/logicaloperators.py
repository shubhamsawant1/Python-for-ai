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
is_child = not is_adult 
print(is_child)