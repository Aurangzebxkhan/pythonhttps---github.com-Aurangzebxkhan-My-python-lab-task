spam=42
cheese=spam
spam=100
print(spam)
print(cheese)
spam=[0,1,2,3,4,5,6,7,8,9]
cheese=spam # the reference is being copied not the list.
cheese[1]='Hello!' # this changes the list value.
print(spam)
print(cheese) # the cheese variable refers to teh same list.
spam[-1]='Apple'
print(spam)
spam[-5]='Bananna'
print(spam)
cheese=spam
print(cheese)
cheese[7]='islamabad'
print(cheese)
