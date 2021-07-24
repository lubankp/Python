
print('entrence', end='')

print('\n')

print('one','two','three', sep='.')

def print_powers(n):
    for x in range(1, n):
        print(f'{x:5d} {x ** 2:5d} {x ** 3:5d} {x ** 4:5d} {x ** 5:5d}')

def print_to_file(n):
    f = open('powers.txt', 'w')
    for x in range(1, n):
        print(f'{x:5d} {x ** 2:5d} {x ** 3:5d} {x ** 4:5d} {x ** 5:5d}', file=f)
    f.close()

def print_to_file2(n):
    with open('powers.txt', 'w') as f:
        for x in range(1, n):
            print(f'{x:5d} {x ** 2:5d} {x ** 3:5d} {x ** 4:5d} {x ** 5:5d}', file=f)

print_to_file2(10)