def spam():
    global eggs
    eggs='spam'

eggs='global'
spam()
print(eggs)

def spam():
    global eggs
    eggs='spam' # ths is the global 

def bacon():
    print(eggs) # this is the global

eggs=42# this is the global

eggs=42#thisis the gloabl
spam()
print(eggs)