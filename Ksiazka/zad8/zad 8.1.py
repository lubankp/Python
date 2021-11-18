# zad 1 - sum of list elements
def fun(list):
    sum = 0
    for x in list:
        try:
           sum += int(x)
        except Exception:
            pass
    return sum

list = ['1','10','ten','tree', '7']

print(fun(list))