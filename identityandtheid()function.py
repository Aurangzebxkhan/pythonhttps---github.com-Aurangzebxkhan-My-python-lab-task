a=id('Aurangzeb') # the returned number will be different on your machine.
print(a)
# Getting the unique identifier for a string
unique_id = id('Khan')
print(unique_id)
# Note: The returned number will be different on your machine.
bacon='Hello'
print(id(bacon))
bacon+='World!' # A new string is made from 'Hello ' and 'World!'.
print(id(bacon)) # bacon now refers to a completely different string.
eggs=['cat','dog']# this creates a new list.
print(id(eggs))
eggs.append('mooose') # append() modfies the list "in place".
print(id(eggs)) # eggs still refers to the same list as before.
eggs=['bat','rat','cow'] # this reats a new list , which , has a new identity.
print(id(eggs)) # eggs now refers to a completely different list

