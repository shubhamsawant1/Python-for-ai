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

