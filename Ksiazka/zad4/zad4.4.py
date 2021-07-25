# write names to file

def print_to_file(list):
    with open('write.txt', 'w') as f:
        print(f"{list[2]}, {list[1]}, {list[0]}", file = f)

name = input("Please enter a name:\n")

print_to_file(name.split())