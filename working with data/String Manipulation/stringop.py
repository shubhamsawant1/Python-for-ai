# String Opearations 

# Concatenation (joining string together)

first_name = 'john'
last_name = 'doe'

# Concatentation using + Operator

full_name = first_name + ' ' + last_name

print(full_name) # Output: john doe

# using f - strings (modern Python way!)
full_name = f"{first_name} {last_name}"
print(full_name) # output: john doe

# Multiple Variable
age = 25 
intro = f"my name is {full_name} and I am {age} years old"
print(intro) # output: my name is john doe and I am 25 years old
