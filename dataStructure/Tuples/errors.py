# Wrong - not a tuple
 
single = (42) 
print(type(single)) # <class 'int'>

# Right - include comma 
single = (42,)

print(type(single))


# Trying to modify tuples

# Wrong - tuples are immutable means cannot be changed

point = (3,5)
point[0] = 4  # TypeError!

# Right - Create a new tuple 

point = (4, point[1])
print(point)
# or convert to list, Modify, Convert back

temp = list(point)
temp[0] = 4
point = tuple(temp)

print(point)