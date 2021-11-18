# zad 2 - rewrite solution

# map function

def fun(x):
    element = 0
    try:
        element = int(x)
    except Exception:
        pass
    return element

def sum(list):
    sum = 0
    for x in list:
        sum += x
    return sum

list1 = ['1','10','ten','tree', '7']

list2 = map(fun, list1)
print(sum(list2))


# filter function

def fun1(x):
    element = 0
    try:
        element = int(x)
    except Exception:
        pass
    return element

def sum1(list):
    sum = 0
    for x in list:
        sum += int(x)
    return sum

list3 = ['1','10','ten','tree', '7']

list4 = filter(fun1, list3)
print(sum1(list4))