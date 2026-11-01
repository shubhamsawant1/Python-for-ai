message  = "I love Python Programming with Python"


# Check if something exists in the string
print("Python" in message) # Output: True
print(message.startswith("I")) # Output: True
print(message.endswith("Python")) # Output: True

# Find position of a string 

print(message.find("Python")) # Output: 7

print(message.count("Python")) # Output: 2

# Replace a string with another string
new_message = message.replace("Python" , "Java")
print(new_message) # Output: I love java programming with java