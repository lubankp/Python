# removing spaces from begin and end of sentence vol.2

def get_sentence():
    return input("Please enter a sentence: \n")


sentence = get_sentence()

list_of_letters = list(sentence)
print(list_of_letters.strip())