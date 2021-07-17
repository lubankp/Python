# find words in sentence

def find(word, sentence):
    return word in sentence


word1 = input("Enter a word1 \n")
word2 = input("Enter a word2 \n")
word3 = input("Enter a word3 \n")
sentence = input("Enter a sentence \n")

print(f"Word1: {find(word1, sentence)}")
print(f"Word2: {find(word2, sentence)}")
print(f"Word3: {find(word3, sentence)}")