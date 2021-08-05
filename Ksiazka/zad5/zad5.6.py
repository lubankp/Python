# dictionary comprehensions

dict = {n: n ** 2 for n in range(10)}

dict2 = {n: n ** 2 for n in range (10 ) if n ** 2 % 2 ==0}

print(dict)
print(dict2)

dict3 = {n ** 2: n for n in range(10)}

dict4 = {n ** 2: n for n in range (10 ) if n ** 2 % 2 ==0}
print(dict3)
print(dict4)