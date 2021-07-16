
def morse_code(data_letter):
    if data_letter == "a":
        return ".- "
    elif data_letter == "b":
        return "-... "
    elif data_letter == "c":
        return "-.-. "
    elif data_letter == "d":
        return "-.. "
    elif data_letter == "e":
        return ". "
    elif data_letter == "f":
        return "..-. "
    elif data_letter == "g":
        return "--. "
    elif data_letter == "h":
        return ".... "
    elif data_letter == "i":
        return ".. "
    elif data_letter == "j":
        return ".--- "
    elif data_letter == "k":
        return "-.- "
    elif data_letter == "l":
        return ".-.. "
    elif data_letter == "m":
        return "-- "
    elif data_letter == "n":
        return "-. "
    elif data_letter == "o":
        return "--- "
    elif data_letter == "p":
        return ".--. "
    elif data_letter == "q":
        return "--.- "
    elif data_letter == "r":
        return ".-. "
    elif data_letter == "s":
        return "... "
    elif data_letter == "t":
        return "- "
    elif data_letter == "u":
        return "..- "
    elif data_letter == "w":
        return ".-- "
    elif data_letter == "x":
        return "-..- "
    elif data_letter == "y":
        return "-.-- "
    elif data_letter == "z":
        return "--.. "
    elif data_letter == "1":
        return ".---- "
    elif data_letter == "2":
        return "..--- "
    elif data_letter == "3":
        return "...-- "
    elif data_letter == "4":
        return "....- "
    elif data_letter == "5":
        return "..... "
    elif data_letter == "6":
        return "-.... "
    elif data_letter == "7":
        return "--... "
    elif data_letter == "8":
        return "---.. "
    elif data_letter == "9":
        return "----. "
    elif data_letter == "0":
        return "----- "
    elif data_letter == " ":
        return "  "

def input_data():
    data_input = input("Write a sentence:\n")
    data_letter = ""
    for letter in data_input:
        data_letter += morse_code(letter)
    return data_letter

print(input_data())

