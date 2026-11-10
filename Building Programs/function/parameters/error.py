# Wrong number of arguments

def greet(name, age):
    print(f"Hi {name}, you're {age}")

# Wrong - too few arguments
greet("Alice")  # TypeError!

# Wrong - too many arguments
greet("Alice", 25, "NYC")  # TypeError!

# Right
greet("Alice", 25)

# Default values with mutable objects
# Wrong - don't use lists as defaults
def add_item(item, list=[]):
    list.append(item)
    return list

# Right - use None and create new list
def add_item(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list
# create a master list to store the items across loop iterations
my_list = []
while True:
    item = input("Enter Item: ")
    # pass the master list in to function and update it
    my_list = add_item(item, my_list)

    if item == "car":
     break

# Final list
print(f"Final List {my_list}")

    