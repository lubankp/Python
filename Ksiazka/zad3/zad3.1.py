# question 1 in chapter 5
# sort words alfabetically

def get_sentence():
    return input("Please enter a sentence: \n")

sentence = get_sentence()
sentence1 = sentence.split()
sentence1.sort()

print(sentence)
print(sentence1)

