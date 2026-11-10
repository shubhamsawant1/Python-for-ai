# Function become powerful when they can accept input. Let's learn about parameters!

# Parameters - Pass data into your function

# without parameters (inflexible)

def greet_alice():
  print("Hello, Alice")

# with parameters (flexible)

def greet(name):
  print(f"Hello, {name}!")

# Now it works for anyone
greet("Alice")
greet("bob")
greet("Charlie")