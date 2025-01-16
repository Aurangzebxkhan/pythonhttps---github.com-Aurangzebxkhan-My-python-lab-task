# Define the original string
name = 'Zophie a cat'

# Replace part of the string by creating a new one
name = name[:7] + 'the' + name[8:]
print(name)  # Output: 'Zophie the cat'




# Define the original string
name = 'Zophie a cat'

# Create a new string by replacing part of the original string
newName = name[0:7] + 'the' + name[8:12]

# Print the original and the new strings
print(name)     # Output: 'Zophie a cat'
print(newName)  # Output: 'Zophie the cat'
