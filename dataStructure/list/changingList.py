# Changing Lists 
# Lists are mutable - you can change them

fruits = ["apple", "banana", "orange"]

# Change an item 
fruits[0] = "mango"

print(fruits) # ["mango", "banana", "orange"]

# Add item

fruits.append("grape") # Add to end
fruits.insert(1, "kiwi") # Insert at position

print(fruits)