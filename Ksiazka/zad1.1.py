# version 1 print_upto
def print_upto(n):
    for x in range(1, n+1):
        print(x, end=' ')

def print_down_from(n):
    for x in range(n, 0, -2):
        print(x, end=' ')

print_upto(10)
print('')
print_down_from(10)