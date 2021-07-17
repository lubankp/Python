def count_spaces(data_string):

    count = 0
    for x in data_string:
       if x == " ":
            count += 1

    print(count)

data_string = input("Hey, user put a string\n")

count_spaces(data_string)