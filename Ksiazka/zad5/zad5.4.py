# union function

def union(dict1, dict2):
    un = {}
    for k, v in dict2.items():
        un[k] = v
    for k, v in dict1.items():
        un[k] = v



    return un

dict1 = {1: 'one', 2: 'two', 5:'eight'}
dict2 = {2: 'three', 3: 'four', 4: 'zero'}

print(union(dict1, dict2))