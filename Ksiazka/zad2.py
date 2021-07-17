l = ['zero', 'one', 'two','three']
l1 = [1, 2]

print(len(l1))
print(type(l1[1]))
print(type(l[1]))

print(l+l1)

for x in l:
    print(x + ' has ' + str(len(x)) + ' letters')

print(l[1:3])
l.append('four')
print(l)
del l[1:3]
print(l)
l.remove('four')
print(l)
l.insert(3,'two')
print('l:' + str(l))
l3 = l.copy()
print('l3:' + str(l3))

print('two' in l)
print(l.index('three'))
print(l.count('zero'))