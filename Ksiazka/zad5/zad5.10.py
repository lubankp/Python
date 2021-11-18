#sum numbers in tuple

def sum(tuple):
    sum = 0
    for x in tuple:
        if type(x) == int:
            sum = sum + x
        else:
            for y in x:
                if type(y) == int:
                    sum = sum + y

    return sum



tuple1 = (1,(1,4),3,(4,2))
sum = sum(tuple1)
print(f'Sum of tuple1 is {sum}')