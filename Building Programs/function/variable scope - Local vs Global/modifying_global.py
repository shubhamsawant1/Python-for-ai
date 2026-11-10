# Modifying global variable

# To change a global variable inside a function, use the global keyword:

counter = 0 # Global variable

def increment():
  global counter # Declare we want to modify the [gloabal] variable

  counter += 1

increment()
increment()

print(counter)  #2

# ! Avoid using [global] when possible. it makes code harder to uunderstand and debug. insted, pass values as parameters and return result.

