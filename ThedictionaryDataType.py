mycat={'size':'fat','color':'gray','dispositin':'loud'}
for key, value in mycat.items():
	print(key)
	print(value)
mycat['size']
print(mycat)
print('my cat has '+mycat['color']+ ' fur.')



myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

# Extracting only keys
keys = list(myCat.keys())

# Extracting only values
values = list(myCat.values())

# Combining keys and values in pairs
combined = list(zip(keys, values))

# Accessing dictionary values through their keys
size = myCat['size']
color_description = 'My cat has ' + myCat['color'] + ' fur.'

# Outputting the results
print("Keys:", keys)
print("Values:", values)
print("Combined:", combined)
print("myCat['size']:", size)
print(color_description)
spam={12345:'Luggage Combination',42:'The Answer'}
a=list(spam.keys())
b=list(spam.values())
print(a)
print(b)
c=list(zip(a,b))
print(c)
