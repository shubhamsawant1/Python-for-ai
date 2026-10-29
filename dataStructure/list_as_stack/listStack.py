# this list methods make it very easy to use a  list as a stack, Where the last element added is the first element re retrived (last-in, first-out). To add an item to the top of the stack, use append()
''' To retrive an  item from the top of the stack, use pop() without an explicit index. For example'''

stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

# Using Lists as Queues 

# it is also possible to usea list as a queue, where the first element added is the first element retrived ("first-in, first-out") however, lists are efficient for efficient for this purpose. While appends and pops from the end of list are fast, doing in-serts or pops from the beginning of a list is slow (because all of the other element have to be shifted by one). See Time complexity of operations on build - in types for more  informaction.  

