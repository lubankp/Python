# fix function, remove zeros

def remove_zeros(l):
   x = 0
   while x != len(l):
        if l[x] == 0:
            del l[x]
        else:
            x += 1


l = [1,0,1,0,0,1,0,1]
remove_zeros(l)
print(l)