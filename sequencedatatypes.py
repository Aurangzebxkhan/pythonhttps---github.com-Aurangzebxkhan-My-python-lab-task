# Define the string
name = 'Zophie'

# Access and print the first character
print(name[0])  # Output: 'Z'

# Access and print the second to last character
print(name[-2])  # Output: 'i'

# Slice and print the string from index 0 to 4 (not including 4)
print(name[0:4])  # Output: 'Zoph'

# Check for substring presence and print results
print('Zo' in name)  # Output: True
print('z' in name)   # Output: False
print('p' not in name)  # Output: False

# Loop through the string and print each character with decoration
for i in name:
    print('* * * ' + i + ' * * *')
# Output:
# * * * Z * * *
# * * * o * * *
# * * * p * * *
# * * * h * * *
# * * * i * * *
# * * * e * * *
