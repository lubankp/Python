# clip function
from random import randint

def clip(x):
    if x < 1:
        return 1
    elif x > 10:
        return 10
    else:
        return x

def clip_list(list):
    list2 = []
    for x in list:
        list2.append(clip(x))

    return list2


number = int(input("Enter a number: \n"))
number2 = clip(number)

print(number2)

list3 = [randint(-10,50), randint(-10,50),randint(-10,50),randint(-10,50),randint(-10,50)]
print(list3)
list4 = clip_list(list3)
print(list4)