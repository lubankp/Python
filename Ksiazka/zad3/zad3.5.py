# palindromic function

def get_word():
    return input("Please enter a word: \n")

def get_sentence():
    return input("Please enter a sentence: \n")

def palindromic(word):
    word1 = str(list(reversed(list(word))))
    word2 = str(list(word))
    if word1 == word2:
        return True
    else:
        return False

def filter_fun(word):
    return palindromic(word)


list_of_words = get_sentence().split()

result = list(filter(filter_fun, list_of_words))

print(result)