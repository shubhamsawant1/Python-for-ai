# Wrong - not a tuple
 
single = (42) 
print(type(single)) # <class 'int'>

# Right - include comma 
single = (42,)

print(type(single))


# Trying to modify tuples

# Wrong - tuples are immutable means cannot be changed

point = (3,5)
print(point)
# point[0] = 4  # TypeError!
# print(point)
# Right - Create a new tuple 

point = (4, point[1])  # Take the first value you want = 4 and get the second value from old tuple point[1]
print(point) # Create complete new tuple (4 ,5)
# or convert to list, Modify, Convert back

temp = list(point) # Converts tuple into list
temp[0] = 4 # Changes first element 
point = tuple(temp) # Coverts list back into tuple / Stores the new tuple in point

print(point)