import copy
spam=['A','B','C','D','E','F','G','H','I']
print(id(spam))
cheese=copy.copy(spam)
print(id(cheese))
cheese[1]=42
print(spam)
print(cheese)
