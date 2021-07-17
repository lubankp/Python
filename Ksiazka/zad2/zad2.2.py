def reverse(list1):
    list2 = list.copy()
    for i, el in enumerate(list1):
        list2[-i-1] = el
    return list2

def reverse2(list1, count):
    list2 = list1[-1:-count:-1]
    return list2

count = 10
list = list(range(1,count))

print(list)
list_rev = reverse(list)
print(list_rev)
list_rev2 = reverse2(list, count)
print(list_rev2)