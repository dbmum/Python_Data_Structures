[Overview](README.md)
# Python Data Structures

## Introduction
As a software engineer I always aim to solve new problems and learn new things. To solve problems I often find that efficiency and how I store my data comes into great importance. In this tutorial I will show how different data structures and taking into consideration the O notation of an operation can make better programs.

## What is a data structure?
A data structure is a way that you can choose to organize your data while programming. A very common example of this is putting data into a list or array. The way that you organize can have different impacts on the performance of a program. In this tutorial I will explain three specific data types, show why they are used, and give examples. These data types are:
### [Stack](stack.md)
### [Set](set.md)
### [Tree](tree.md)

## O notation
O notation is a way to describe the efficiency of a program based off of how many operations it will take if there was more data going through the program. with small amounts of data, the design of your program and data structures may not affect the overall efficiency much, but as you think about putting millions of points of data through your code how will efficiency stack up?

![O Notation graph](O-notation-graphic.png)

We can see that a O(1) operation is the best type, that no matter how much data you have it will always be one operation, for example to find the size of a list on python you can use the len() built-in-function. The length of a list is stored seperately with the list, so calling upon it is always one operation, even if the list was 1 million items long

```Python
my_list = [1, 2, 3, 4, 5]
print(len(my_list))
# 5
# number of operations = 1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(len(my_list))
#15
# number of operations = 1
```

Following the size example, say we wanted to instead loop through our list and count each item that way, this would be considered a O(n) operation. The more data we have, the longer it will take proportianally. As data input increases, so does the number of operations occuring.

```Python
my_list = [1,2,3,4,5]
count = 0

for item in my_list:
    count += 1

print(count)
# 5
# number of operations = 5

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
count = 0

for item in my_list:
    count += 1

print(count)
# 15
# number of operations = 15
```

We can see how based off of how you use loops you can quickly increase the number of operations performed by a program. Below is an example of how you would get a O(n^2) performance with nested loops. For each nested loop you decrease in operation efficiency (n^2, then n^3, then n^4, etc).

```python
my_list = [1,2,3,4,5]
my_check_list = [1,2,3,4,5]
count = 0

#  loop that checks to see if each value is in the check list
for item in my_list:
        for check in my_check_list:
            if item == check:
                count += 1

print(count)
# 5
# number of operations = 25


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
my_check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
count = 0

#  loop that checks to see if each value is in the check list
for item in my_list:
        for check in my_check_list:
            if item == check:
                count += 1

print(count)
# 15
# number of operations = 225
```

## Conclusion
In the tutorial I hope that you will be able to better understand how data structures can effect the performance of your programs. You will be able to see the impacts of O Notation, and practice with each data structure using these structures.

[Overview](README.md)