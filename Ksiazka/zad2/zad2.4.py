def setify(list):
    for i in list:
        dublication = list.count(i)
        if dublication != 1:
            for x in range(0,dublication-1):
                list.remove(i)
    return list

list = [1, 2, 1, 3, 1 ,4, 5, 6, 4, 2, 2, 1]
print(list)
print(setify(list))