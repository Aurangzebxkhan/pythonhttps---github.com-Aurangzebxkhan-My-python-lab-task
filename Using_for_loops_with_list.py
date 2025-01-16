# for i in [0, 1, 2, 3]:
#     print(i)
# Define the list
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

# Loop through the list and print the index and corresponding item
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])



# the in and not in operators
# Check if 'howdy' is in the list
is_in_list = 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
print(is_in_list)  # Output: True

# Define the list
spam = ['hello', 'hi', 'howdy', 'heyas']

# Check if 'cat' is in the list
is_cat_in_list = 'cat' in spam
print(is_cat_in_list)  # Output: False

# Check if 'howdy' is not in the list
is_howdy_not_in_list = 'howdy' not in spam
print(is_howdy_not_in_list)  # Output: False

# Check if 'cat' is not in the list
is_cat_not_in_list = 'cat' not in spam
print(is_cat_not_in_list)  # Output: True




# Define the list of pet names
myPets = ['Zophie', 'Pooka', 'Fat-tail']

# Prompt the user to enter a pet name
print('Enter a pet name:')
name = input()

# Check if the entered name is in the list of pets
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')



# the multiple Assigement Rrick
# Define the list
cat = ['fat', 'gray', 'loud']

# Assign elements of the list to variables
size = cat[0]
color = cat[1]
disposition = cat[2]

# Print the variables
print(size)        # Output: 'fat'
print(color)       # Output: 'gray'
print(disposition) # Output: 'loud'




# Using the enumerate() Function with Lists
# Define the list
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

# Loop through the list with index and item using enumerate
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)





#using the random.choice() and random.shuffle()
# Import the random module
import random

# Define the list of pets
pets = ['Dog', 'Cat', 'Moose']

# Select a random pet from the list
random_pet = random.choice(pets)
print(random_pet)  # Output will be a random choice from the list, e.g., 'Dog', 'Cat', or 'Moose'

# You can run the choice multiple times to see different random selections
random_pet = random.choice(pets)
print(random_pet)  # Output will be a random choice from the list, e.g., 'Dog', 'Cat', or 'Moose'

random_pet = random.choice(pets)
print(random_pet)  # Output will be a random choice from the list, e.g., 'Dog', 'Cat', or 'Moose'


# Import the random module
import random

# Define the list of people
people = ['Alice', 'Bob', 'Carol', 'David']

# Shuffle the list randomly
random.shuffle(people)
print(people)  # Output will be a shuffled list, e.g., ['Carol', 'David', 'Alice', 'Bob']

# Shuffle the list again to see a different random order
random.shuffle(people)
print(people)  # Output will be a shuffled list, e.g., ['Alice', 'David', 'Bob', 'Carol']

