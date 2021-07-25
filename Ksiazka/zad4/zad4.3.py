# print powers

def print_powers(n):
    for x in range(1, n):
        print(
            f'{str(x).zfill(5).rjust(5)} {str(x ** 2).zfill(5).rjust(5)} {str(x ** 3).zfill(5).rjust(5)} {str(x ** 4).zfill(5).rjust(5)} {str(x ** 5).zfill(5).rjust(5)}')


print_powers(10)
