# Morse code second wersion
def morse_code(data_letter):
    list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " "]
    list2 = [".- ", "-... ", "-.-. ", "-.. ", ". ", "..-. ", "--. ", ".... ", ".. ", ".--- ", "-.- ", ".-.. ", "-- ",
             "-. ", "--- ", ".--. ", "--.- ", ".-. ", "... ", "- ", "..- ", ".-- ", "-..- ", "-.-- ", "--.. ",".---- ",
             "..--- ", "...-- ", "....- ", "..... ", "-.... ", "--... ", "---.. ", "----. ", "----- ", "   "]
    element = ""
    for i, el in enumerate(list1):
        if data_letter == el:
             element = list2[i]

    return element

def input_data():
    data_input = input("Write a sentence:\n")
    data_letter = ""
    for letter in data_input:
        data_letter += morse_code(letter)
    return data_letter

print(input_data())