# Variable in python have a "scope" - where they can be accessed and used.

# Local variable
""" Variable created inside a function only exist within that function: """

def calculate_price():
  price = 100
  tax = price * 0.1
  print(f"Total: {price + tax}")

calculate_price() # calling function