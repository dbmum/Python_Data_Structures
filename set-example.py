"""
Set Example
"""

import random

# Create an empty set
from os import remove


my_set = set()
print(my_set)

# Add
my_set.add(7)
my_set.add(3)
my_set.add(0)

print(my_set)


# Remove
my_set.remove(3)
print(my_set)

# member
if 7 in my_set:
    my_set.remove(7)
else:
    my_set.add(7)

print(my_set)

if 9 in my_set:
    my_set.remove(9)
else:
    my_set.add(9)

print(my_set)

# Size
length = len(my_set)
print(f"length = {length}")

to_add = [1,2,3,4,5,6,7,8,10]

for number in to_add:
    my_set.add(number)

length = len(my_set)
print(my_set)
print(f"length = {length}")


print('\
    \n******************\
    \nPractical example\
    \n******************')
"""
In this example we are trying to count the 
number of duplicates in our list using O(n)
performance.
"""
#Practical example
randomlist = []
for i in range(0,45):
    n = random.randint(0,30)
    randomlist.append(n)
print('\nOur random list:')
print(randomlist)

unique_values = set(randomlist)

number_of_duplicates = len(randomlist) - len(unique_values)

print(f'\nThe number of duplicates in the list = {number_of_duplicates}')
print('Unique values - {}'.format(unique_values))
find_number = int(input("\nEnter a number to see if it is in the set: \n"))

if find_number in unique_values:
    print('That number is in the set!')
else:
    print('Sorry, that number is not in the set')