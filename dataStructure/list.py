# the list data type has some more methods. Here are all of the methods of list objects:

list = ["shubham", "karan", "viraj", "sahil", "nikhil"]
list2 = [22,56,8,5,46,9,5,4]
list.append("niraj") # add an items to the list. Similar to a[len(a):] = [x]

print(list)

list.extend(list2)
# Extend the list by appending all the items from the iterable. Similar to a[len(a):] = iterable
print(list)

list.insert(0 , "sidharth")
# insert an item at given position. The first argument is the index of the element before which to in - sert, so a.insert (0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

print(list)

list.remove("shubham")
# Remove the first item from the list whose value is equal to value. it raises a ValueError if there is no such item.

print(list)

list.pop(-1)
# Remove the item at the given position in the list, And return it,  if no index is specified, a.pop() removes and returns the last item in the list. it raises an IndexError if the list is empty or the index is outside the list range. 

print(list)

# list.clear()
# # Remove all items from the list, Similar to del a[] gives empty list

# print(list)

print(list.index("nikhil", 0))
# # Return zero-based index of the first and end are interpreted as in the slice notation and are used to limit the search to a particular subsequance of the list,  the returned index is computed relative to the beginning of the sequence rather than the start argument.

numbers = [10,20,40,50,60,23,45,78,95,41]

# search for 20, starting the search at index 2
# It skips the 20 at index 1 and finds the 20 at index 3

print(numbers.index(20, 0))

# Search for 20 between index 2 and index 4 (index 4 is excluded)

print(numbers.index(20, 0, 4))

count = numbers.count(20)
# Return the number of times value appears in the list.
print(f"count: {count} ")

fruits = ["banana", "Apple", "mango", "grape", "orange", "pear"]
# sort the items of the list in place ( the argument can be used for sort custmization, see sorted() for their explanation)
fruits.sort(reverse=True)
print(fruits)

fruits.reverse()
# Reverse the element of the list in place 

print(fruits)

myfruits = fruits.copy()
# Return a shallow copy of the list. Similar to a[:]
print(myfruits)

# examples that use most of the list methods

fruit = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print(fruit.count('apple'))

print(fruit.count('tangerine'))

print(fruit.count('banana'))

print(fruit.index('banana'))

fruit.reverse()

print(fruit)

fruit.append('mango')
print(fruit)

fruit.insert(2, 'banana')
print(fruit)

fruit.sort(reverse=False)
print(fruit)

newNumber = [20, 50, 40, 70, 80, 60]

newNumber.sort(reverse=True)
print(newNumber)