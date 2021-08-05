#chapter7: tuples, dictionaries, sets

#touple - immutable
t = (1, 'one')
t2 = (1, (1,2),(1, 2, 3))

a, b = t
print(a)
print(b)
c, d, e = t2
print(c)
print(d)
print(e)

# function

def f(x):
    a, b = x
    return a + b

pair = (1, 2)
result = f(pair)
print (result)

print(t2[1])
# from back
print(t2[::-1])

# changing value of list inside touple
list = [1, 2, 3]
t4 = (list, list)
list[0] = 5
print(t4)

#dictionaries

d = {1: 4, 2: 3, 3: 2}
print(d)
del d[2]
print(d)
d[2] = 3
d[4] = 7
d[5] = 10

for k, v in d.items():
    print(f'{k} is mapped to {v}')

for k in d:
    print(f'{k} is mapped to {d[k]}')

#sets

s2 = set([1,2,3,2,1])
print(s2)
s3 = set('qwertyuiop')
print(s3)
s3.add('a')
print(s3)
s2.remove(2)
print(s2)

a = {1,2,3,4}
b = {1,2,5,6}
print(a | b)
print(a & b)
print(a ^ b)
print(a - b)

