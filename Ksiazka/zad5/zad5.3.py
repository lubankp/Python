# zip function


def zip(list1,list2):
    dict = {}
    for i, el in enumerate(list1):
        dict[el] = list2[i]
    return dict


list1 = [1,2,3,4,5]
list2 = ['one', 'four', 'five', 'six', 'seven']

print(zip(list1, list2))