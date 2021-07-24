# chapter 5

#def join(l):
#    s = ''
#    for x in l:
#        s += x
#    return s

l = list('listaliter')
f = str(l)
g = ''.join(l)

print(l)
print(f)
print(g)

t = 'to jest zdanie'
w = t.split()

print(w)
print(t.find('jest'))

lista = [5,2,7,4,1,1,5]
sorted_lista = sorted(lista)
lista.sort()
print(lista)
print(sorted_lista)

def squere(x):
    return x*x
l_map = list(map(squere,lista))
print(l_map)

def even(x):
    return x % 5 == 0

l_even = list(filter(even, lista))
print(l_even)

for x in map(squere,lista):
    print(x)

rev_list = reversed(lista)
for x in rev_list:
    print(x)
# list comprehension

compr_1 = [x*x for x in range(10)]
print(compr_1)

compr_2 = [str(x) for x in range(10)]
print(compr_2)

compr_3 = [x % 3 == 0 for x in range(20)]
print(compr_3)

compr_4 = [x*x*x for x in range(20) if (x*x*x) % 2 == 0]
print(compr_4)

#common problems

z = "marginal"
z1 = " "
z3 = z1.join(z)
z4 = z.join(z1)
print(z3)
print(z4)