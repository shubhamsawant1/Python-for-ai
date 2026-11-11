# Getting result from function - so far, out function have printed output. But often you want functions to calculate something and give you the result to use elsewhere.

# This function only prints

def add_print(a, b):
  print(a + b)

#This function returns a value

def add_returns(a, b):
  return a + b

# Now you can use the result
result = add_returns(5, 3)
print(f"The result is {result}") # the result is 8