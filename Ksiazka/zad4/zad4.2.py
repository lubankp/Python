# print powers

def print_powers(n):
    for x in range(1, n):
        print(f'{str(x).rjust(5)} {str(x ** 2).rjust(5)} {str(x ** 3).rjust(5)} {str(x ** 4).rjust(5)} {str(x ** 5).rjust(5)}')


print_powers(10)