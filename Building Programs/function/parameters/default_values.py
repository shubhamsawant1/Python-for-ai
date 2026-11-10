# Give parameters default values for optional arguments

def greet(name, greeting="hello"):
  print(f"{greeting}, {name}!")

# use default

greet("Bob") # hello, Alice

# Override default
greet("Bob", "Hi") # Hi, bob

greet("Charlie", "Hey") #Hey, Charlie
