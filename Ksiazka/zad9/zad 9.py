# read from file

f = open('gregor.txt', 'r')
for line in f:
    print(line, end='')
f.close()

# list of lines
f = open('gregor.txt', 'r')
print('\n')
list1 = list(f)
print(list1)
f.close()

# reversed list of lines
for line in reversed(list1):
    print (line)

# write to file reversed list

f_out = open('output.txt', 'w')
for line in reversed(list1):
    print (line, end = '', file = f_out)

f_out.close()

# shorter wersion write to file

with open('gregor.txt', 'r') as f, open('output1.txt', 'w') as f_out:
    for line in reversed(list(f)):
        print(line, end='', file=f_out)

# statistics from file

def sentence_end(elem):
    return (elem == '.' or elem == '!')

def statistics_from_file (file):

    lines = 0
    characters = 0
    words = 0
    sentences = 0
    for line in file:
        lines += 1
        characters += len(line)
        words += len(line.split())
        sentences += len(list(filter(sentence_end, line)))

    return (lines, characters, words, sentences)

file1 = open('gregor.txt', 'r')
print(statistics_from_file(file1))
