list=[1,2,3]
print(list)

list_1=['cat','bat','rat','elephant']
print(list_1)

list_2=['hello','3.1415',True,None,42]
print(list_2)



spam=['cat','bat','rat','elephant']
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])




# Define the nested list
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]

# Access the first element of spam
first_element = spam[0]
print(first_element)  # Output: ['cat', 'bat']

# Access the second element of the first nested list
second_element_first_list = spam[0][1]
print(second_element_first_list)  # Output: 'bat'

# Access the fifth element of the second nested list
fifth_element_second_list = spam[1][4]
print(fifth_element_second_list)  # Output: 50



# Define the list
spam = ['cat', 'bat', 'rat', 'elephant']

# Access the last element using a negative index
last_element = spam[-1]
print(last_element)  # Output: 'elephant'
print(spam[-1]) # also wire it okay 
# Access the third element from the end using a negative index
third_element_from_end = spam[-3]
print(third_element_from_end)  # Output: 'bat'

# Create a sentence using elements from the list
sentence = 'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'
print(sentence)  # Output: 'The elephant is afraid of the bat.'




# Getting a list from another list with Slices
# Define the list
spam = ['cat', 'bat', 'rat', 'elephant']

# Slice the list from index 0 to 4 (not including 4)
slice1 = spam[0:4]
print(slice1)  # Output: ['cat', 'bat', 'rat', 'elephant']

# Slice the list from index 1 to 3 (not including 3)
slice2 = spam[1:3]
print(slice2)  # Output: ['bat', 'rat']

# Slice the list from index 0 to the second to last element
slice3 = spam[0:-1]
print(slice3)  # Output: ['cat', 'bat', 'rat']


# Define the list
spam = ['cat', 'bat', 'rat', 'elephant']

# Slice the list from the start to index 2 (not including 2)
slice1 = spam[:2]
print(slice1)  # Output: ['cat', 'bat']

# Slice the list from index 1 to the end
slice2 = spam[1:]
print(slice2)  # Output: ['bat', 'rat', 'elephant']

# Slice the entire list
slice3 = spam[:]
print(slice3)  # Output: ['cat', 'bat', 'rat', 'elephant']



spam=['cat','dog','moose']
print(len(spam))






# Define the list
spam = ['cat', 'bat', 'rat', 'elephant']

# Change the second element to 'aardvark'
spam[1] = 'aardvark'
print(spam)  # Output: ['cat', 'aardvark', 'rat', 'elephant']

# Change the third element to the value of the second element
spam[2] = spam[1]
print(spam)  # Output: ['cat', 'aardvark', 'aardvark', 'elephant']

# Change the last element to 12345
spam[-1] = 12345
print(spam)  # Output: ['cat', 'aardvark', 'aardvark', 12345]



# Concatenate two lists
concatenated_list = [1, 2, 3] + ['A', 'B', 'C']
print(concatenated_list)  # Output: [1, 2, 3, 'A', 'B', 'C']

# Repeat a list three times
repeated_list = ['X', 'Y', 'Z'] * 3
print(repeated_list)  # Output: ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

# Define a list and concatenate with another list
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)  # Output: [1, 2, 3, 'A', 'B', 'C']



# Define the list
spam = ['cat', 'bat', 'rat', 'elephant']

# Delete the third element (index 2)
del spam[2]
print(spam)  # Output: ['cat', 'bat', 'elephant']

# Delete the new third element (index 2)
del spam[2]
print(spam)  # Output: ['cat', 'bat']



#Working With lists
# Initial cat names
catName1 = 'Zophie'
catName2 = 'Pooka'
catName3 = 'Simon'
catName4 = 'Lady Macbeth'
catName5 = 'Fat-tail'
catName6 = 'Miss Cleo'

# Prompting user to enter the names of the cats
print('Enter the name of cat 1:')
catName1 = input()
print('Enter the name of cat 2:')
catName2 = input()
print('Enter the name of cat 3:')
catName3 = input()
print('Enter the name of cat 4:')
catName4 = input()
print('Enter the name of cat 5:')
catName5 = input()
print('Enter the name of cat 6:')
catName6 = input()

# Printing the entered cat names
print('The cat names are:')
print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' + catName5 + ' ' + catName6)

# Initialize an empty list for cat names
catNames = []

# Start an infinite loop to get cat names from the user
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    # Concatenate the new cat name to the list
    catNames = catNames + [name]

# Print the cat names
print('The cat names are:')
for name in catNames:
    print('  ' + name)

