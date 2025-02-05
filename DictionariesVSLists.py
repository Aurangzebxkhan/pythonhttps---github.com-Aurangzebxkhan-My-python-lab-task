# Comparing lists
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)  # Outputs: False
a=['a','b','c','d']
b=['d','c','b','a']
print(a==b)
d=['a','b','c','d']
f=['a','b','c','d']
print(d==f)
# now the both same therefor it become true 

# Comparing dictionaries
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)  # Outputs: True
z = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
x = {'age': '8', 'species': 'cat', 'name': 'Zophie'}
print(z==x)
o = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
p= {'8': 'age', 'cat': 'species', 'Zophie': 'name'}
print(o==p)
