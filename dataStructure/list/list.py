# List

# empty list 

my_list = []

# Assuming my_list already exists
for i in range(5):
    item = input("Enter the item you want to add in list: ")
    my_list.append(f"item_{item}") 


print(my_list)

# list with items 
fruits = ["apple", "banana" , "orange"]

number = [1,2,3,4,5,6,7,8,9,10]

mixed = ["hellow" , 48, "True" , 3.14]


# ! Lists use square brackets [] and items are separed by commas. You can mix different data types in the same list!

# Accessing items 

fruits = ["apple" , "banana", "orange"]

# Get items  
print(fruits[0]) # apple (first item)

print(fruits[1]) # "banana
print(fruits[-1]) # orange (last item)

print(fruits[-2]) # "banana" second to last

# Slicing 

print(fruits[0:2]) # ["apple", "banana"]

print(fruits[1:]) # ["banana", "orange"]