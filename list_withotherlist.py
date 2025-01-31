spam=[['cat','bat'],[10,20,30,40,50]]
print(spam[0])
print(spam[0][1])
print(spam[1][4])
print(spam[1][0])

spam=['cat','bat','rat','elephant']
print(spam[-1])
print(spam[-3])
print('the '+spam[-1]+' is afraid of the '+spam[-3]+' .')
print(spam[1:4])
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])
print(spam[:2])
print(spam[1:])
print(spam[:])
#getting a list's length with the len() function
spam=['cat','dog','moose']
print(len(spam))
#changing Values in a list with indexes
spam=['cat','bat','rat','elephant']
spam[1]='aardvark'
print(spam)
spam[2]=spam[1]
print(spam)
spam[-1]=12345
print(spam)
spam=[1,2,3]+['A','B','C','D']
print(spam)
spam=['X','Y','Z']*3
print(spam)
spam=[1,2,3]
spam=spam+['A','B','C']
print(spam)
#Removing Values from list with del statements
spam=['cat','bat','rat','elephant']
del spam[2]
print(spam)
del spam[2]
print(spam)




