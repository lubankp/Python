
def fun_letter(list):
    str1 = ''
    for i, word in enumerate(list):
        str1 = str1 + word
    return set(str1)

list = ["one", "two", "three", "four", "five"]

print(fun_letter(list))