# Python throws an error if the item doesn't exits, it is a best practice to check if the item is in the list, or wrap your code in a try/except block.

names = ["Alice", "Bob", "Charlie"]

# Safe approach using 'in'
name = input("Enter Name: ")
if name in names:
  print(names.index(name))
else:
  print("Item not Found!")

# Safe appoach using try/except

try:
  print(names.index(name))
except ValueError:
  print('Item not Found!')