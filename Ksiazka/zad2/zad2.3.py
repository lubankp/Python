# get minimal and maximal element of list

from random import randint

def min(list):
    min = 101
    for i in list:
        if min > int(i):
           min = int(i)
    return min

def max(list):
    max = 0
    for i in list:
        if max < int(i):
           max = int(i)
    return max

list = []
for i in range(0,10):
    list.append(randint(1,100))

print(list)
print(min(list))
print(max(list))