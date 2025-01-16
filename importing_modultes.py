# import random
# for i in range(5):
#     print(random.randint(1,10))



# import random,sys,os,math 
import random
import sys
import os
import math

# Using random to generate random numbers
print("Random numbers between 1 and 10:")
for i in range(5):
    print(random.randint(1, 10))

# Using sys to get the size of an object
sample_list = [1, 2, 3, 4, 5]
print("\nSize of sample_list object:", sys.getsizeof(sample_list), "bytes")


# Find the size of the object 1
size_of_one = sys.getsizeof(1)
print('Size of the object 1:', size_of_one, 'bytes')

# Using os to get the current working directory
print("\nCurrent working directory:", os.getcwd())

# Using math to calculate the square root of a number
number = 16
print("\nSquare root of", number, "is", math.sqrt(number))
