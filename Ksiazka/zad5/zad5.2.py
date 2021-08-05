# unzip function

def unzip(dict):
    list1 = []
    list2 = []
    touple = (list1,list2)
    for k, v in dict.items():
        print(k,v)
        list1.append(k)
        list2.append(v)
    return touple


dict = {1: 'one',2: 'two',3: 'three'}
print(unzip(dict))