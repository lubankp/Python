def reverse(list1):
    list2 = list.copy()
    for i, el in enumerate(list1):
        list2[-i-1] = el
    return list2

list = list(range(1,10))

print(list)
list_rev = reverse(list)
print(list_rev)