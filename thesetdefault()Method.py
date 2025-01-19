# Create a dictionary
spam = {'name': 'Pooka', 'age': 5}

# Use the setdefault() method to set a default value if the key does not exist
spam.setdefault('color', 'black')

# The dictionary now has the 'color' key with the value 'black'
print(spam)

# If the key already exists, setdefault() returns the existing value and doesn't change it
spam.setdefault('color', 'white')

# The dictionary remains unchanged as the 'color' key already exists
print(spam)



message='it was a bright cold day in April, and the clock were striking thirteen.'
count={}
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1
print(count)