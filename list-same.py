s=[{'name':'pooka_1','age':3} ,{'name': 'Pooka', 'age': 5,'name':'pooka_2'}]
print(s)
for item in s:
    for key, value in item.items():
        print(f"{key}: {value}")
        print(key)
        print(value)

b=[{'Name':'khan_0','age':'5','Name':'khan_1','age':'10','Name':'khan_2','age':'15'}]
for item in b:
	for key, value in item.items():
		print(f"{key}: {value}")
for item in b:
    for key in item.keys():
        print(f"{key}")
for item in b:
    for value in item.values():
        print(value)
