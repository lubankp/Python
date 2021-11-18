def or1(dict1, dict2):
    dict3 = {}
    for key, value in dict1.items():
        dict3[key] = value
    for key, value in dict2.items():
        if dict3[key] == 0:
            dict3[key] = value
    return dict3


def and1(dict1, dict2):
    dict3 = {}
    for key, value in dict1.items():
        if value == 1 and dict2[key] == 1:
            dict3[key] = value

    return dict3

def xor1(dict1, dict2):
    dict3 = {}

    for key, value in dict1.items():
        if value == 1:
            dict3[key] = value
    for key, value in dict2.items():
        if value == 1:
            dict3[key] = value
            if dict1[key] == value:
                del dict3[key]

    return dict3

def anotb(dict1, dict2):
    dict3 = {}
    for key, value in dict1.items():
        if value == 1:
            dict3[key] = value
    for key, value in dict2.items():
        if value == 1:
            if dict1[key] == value:
                del dict3[key]

    return dict3

dict1 = {1: 1, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0}
dict2 = {1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}

print(or1(dict1, dict2))
print(and1(dict1, dict2))
print(xor1(dict1, dict2))
print(anotb(dict1, dict2))