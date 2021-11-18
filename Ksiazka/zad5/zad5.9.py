def and1(set1,set2):
    set3 = ([x for x in set1 for y in set2 if x == y])
    return set3

set1 = set([2,2,3,4,4,7])
set2 = set([2,3,6,5,4])

set4 = and1(set1, set2)

print(set1)
print(set2)
print(set4)
