# Create a dictionary
spam = {'color': 'red', 'age': 42}
print(spam)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)
# Iterate through the values of the dictionary and print each one
for v in spam.values():
    print(v)
for a in spam.keys():
    print(a)
for key, value in spam.items(): 
    print("Key:"+ key+" Value:"+  str(value))
