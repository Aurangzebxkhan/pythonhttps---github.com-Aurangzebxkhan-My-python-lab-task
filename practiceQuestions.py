# 1. What is []?
# An empty list

# 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
spam = [2, 4, 6, 8, 10]
spam[2] = 'hello'  # Use indexing to assign 'hello' at the third position
print(spam)

# For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].
spam = ['a', 'b', 'c', 'd']

# 3. What does spam[int(int('3' * 2) // 11)] evaluate to?
result = spam[int(int('3' * 2) // 11)]  # Result is 'd' because '3' * 2 is '33', int('33') is 33, 33 // 11 is 3, so spam[3] is 'd'
print(result)

# 4. What does spam[-1] evaluate to?
result = spam[-1]  # Result is 'd' because -1 index represents the last item in the list

# 5. What does spam[:2] evaluate to?
result = spam[:2]  # Result is ['a', 'b'] because slicing from start to index 2 (excluding index 2) gives the first two elements
print(result)

# For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].
bacon = [3.14, 'cat', 11, 'cat', True]

# 6. What does bacon.index('cat') evaluate to?
index = bacon.index('cat')  # Result is 1 because 'cat' first appears at index 1

# 7. What does bacon.append(99) make the list value in bacon look like?
bacon.append(99)  # bacon becomes [3.14, 'cat', 11, 'cat', True, 99] because append adds an item to the end of the list

# 8. What does bacon.remove('cat') make the list value in bacon look like?
bacon.remove('cat')  # bacon becomes [3.14, 11, 'cat', True, 99] because remove removes the first occurrence of 'cat'
print(bacon)

# 9. What are the operators for list concatenation and list replication?
# List concatenation: + (e.g., [1, 2] + [3, 4] = [1, 2, 3, 4])
# List replication: * (e.g., [1, 2] * 2 = [1, 2, 1, 2])

# 10. What is the difference between the append() and insert() list methods?
# append() adds an item to the end of the list
# insert() adds an item at a specified index

# 11. What are two ways to remove values from a list?
# Using remove() method and using del statement (e.g., del list[index])

# 12. Name a few ways that list values are similar to string values.
# Both are sequences, can be indexed, sliced, and used in loops

# 13. What is the difference between lists and tuples?
# Lists are mutable (can be changed), tuples are immutable (cannot be changed)

# 14. How do you type the tuple value that has just the integer value 42 in it?
tuple_value = (42,)  # Use a comma to define a single value tuple
print(tuple_value)

# 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
tuple_form = tuple([1, 2, 3])  # Using tuple() function
list_form = list((1, 2, 3))  # Using list() function
print(list_form)
print(tuple_form)

# 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
# They contain references to list objects

# 17. What is the difference between copy.copy() and copy.deepcopy()?
# copy.copy() creates a shallow copy (copy of the object only)
# copy.deepcopy() creates a deep copy (copy of the object and all nested objects)
