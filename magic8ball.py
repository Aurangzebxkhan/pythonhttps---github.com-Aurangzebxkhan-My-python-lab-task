import random
messages=['It is certain','It is decidedly so','Yes definitely','Replay hazy try again','Ask again later','Concentrate and ask again','My reply is no','Oulook not so good','Very doubtufl']
print(messages[random.randint(0,len(messages)-1)])


name = 'Zophie'

print(name[0])    # Output: 'Z'
print(name[-2])   # Output: 'i'
print(name[0:4])  # Output: 'Zoph'

print('Zo' in name)  # Output: True
print('z' in name)   # Output: False
print('p' not in name)  # Output: False

for i in name:
    print('* * * ' + i + ' * * *')
