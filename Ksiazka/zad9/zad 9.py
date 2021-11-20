# read from file

f = open('gregor.txt', 'r')
for line in f:
    print(line, end='')

# list of lines
f = open('gregor.txt', 'r')
print('\n')
list1 = list(f)
print(list1)


# reversed list of lines
for line in reversed(list1):
    print (line)