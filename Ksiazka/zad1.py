
def times_table(n):
    for y in range(1, n+1):
        for x in range(1, n+1):
            print(x*y, end='\t')
        print ('')

def times_table1(n):
    column_width = len(str(n*n)) +1
    for y in range(1, n+1):
        for x in range(1, n+1):
            print(x*y, end=' ' * (column_width - len(str(x*y))))
        print ('')

times_table(5)
times_table1(5)