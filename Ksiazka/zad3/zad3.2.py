# removing spaces from begin and end of sentence

def get_sentence():
    return input("Please enter a sentence: \n")

def split(sentence):
    return sentence.split()

def remove_space(list_of_letters):

    while (list_of_letters[-1] == " "):
        del list_of_letters[-1]
        remove_space(list_of_letters)
    return list_of_letters

sentence = get_sentence()
list_of_letters = list(sentence)
print(list_of_letters)

list_of_letters1 = remove_space(list_of_letters)

list_of_letters2 = list(reversed(list_of_letters1))
list_of_letters3 = remove_space(list_of_letters2)
list_of_letters4 = list(reversed(list_of_letters3))
print(list_of_letters4)