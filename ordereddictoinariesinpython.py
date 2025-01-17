# Example demonstrating dictionary behavior in Python

# Create dictionaries
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs['name']
ham['species']
# Print list of dictionary keys
print(list(eggs))  # Output: ['name', 'species', 'age']
print(list(ham))   # Output: ['species', 'age', 'name']
Keys_list=list(eggs)
print(Keys_list[0])
print(Keys_list[1])
values_list=list(ham)
print(values_list[0])
print(values_list[1])
# Note: Dictionaries in Python 3.6+ preserve insertion order, but don't rely on this in older versions

# # Example in older versions of Python (e.g., Python 3.5)
# spam = {}
# spam['first key'] = 'value'
# spam['second key'] = 'value'
# spam['third key'] = 'value'

# # Print list of dictionary keys in an unspecified order (Python 3.5 example)
# print(list(spam))  # Output might be: ['first key', 'third key', 'second key']


# eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
# print(list(eggs))  # Output: ['name', 'species', 'age']

# ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
# print(list(ham))   # Output: ['species', 'age', 'name']


# spam = {}
# spam['first key'] = 'value'
# spam['second key'] = 'value'
# spam['third key'] = 'value'
# print(list(spam))  # Output might be: ['first key', 'third key', 'second key']
# # Modern dictionaries (Python 3.7+)
# eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
# print(list(eggs))  # Output: ['name', 'species', 'age']

# ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
# print(list(ham))   # Output: ['species', 'age', 'name']

# # Older dictionaries (Python 3.5)
# spam = {}
# spam['first key'] = 'value'
# spam['second key'] = 'value'
# spam['third key'] = 'value'
# print(list(spam))  # Output might be: ['first key', 'third key', 'second key']
