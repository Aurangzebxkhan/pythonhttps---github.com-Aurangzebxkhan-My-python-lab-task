for i in range(4):
    print(i)
# for i in [0,1,2,3]:
#     print(i)
supplies=['pens','staplers','flamethrowers','binders']
for i in range (len(supplies)):
    print('Index'+str(i)+'in supplies is:'+supplies[i])


# Check if specific strings are in the list
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])  # True

# Assign the list to the variable
spam = ['hello', 'hi', 'howdy', 'heyas']

# Check for presence of 'cat' in the list
print('cat' in spam)  # False

# Check if 'howdy' is not in the list
print('howdy' not in spam)  # False

# Check if 'cat' is not in the list
print('cat' not in spam)  # True

# the in and not in operators
myPets=['cat','dog','elephent']
print("Enter a pet name:")
name=input()
if name not in myPets:
    print('I do not have a pet named'+name)
else:
    print(name+'is my pet.')

# the multiple assignement trick
cat=['fat','gary','loud']
size=cat[0]
color=cat[1]
dispostition =cat[2]
#you could type this line of code
cat=['fat','gray','loud']
size,color,dispostition=cat
print(cat)