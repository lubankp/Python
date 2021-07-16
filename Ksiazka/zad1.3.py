# spaces without last space
def print_spaced(s):
    length = len(s)
    print(length)
    y = 1
    for x in s:
        if y != length:
            print(x, end=' ')
        else:
            print(x)
        y += 1

data_input = input("Put a string:\n")

print_spaced(data_input)