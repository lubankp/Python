# Caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'v','x', 'y', 'z']
alphabet2 = []
def rotate_alphabet(nun_rotation):
    alphabet_rot = alphabet.copy()
    list_length = len(alphabet)
    for i in range(0, list_length):
        if i+int(number_rotation) < list_length:
            alphabet_rot[i] = alphabet[i + int(number_rotation)]
        else:
            alphabet_rot[i] = alphabet[i + int(number_rotation) - list_length]

    return alphabet_rot

def cripter(sentence, alphabet_rot):
    sentence2 = ''
    for i , el in enumerate(sentence):
        for x , letter in enumerate(alphabet):
            if el == letter:
                sentence2 += str(alphabet_rot[x])
        if el == ' ':
            sentence2 += ' '
    return sentence2

def decripter(sentence):
    sentence3 = ''
    for i, el in enumerate(sentence):
        for x, letter in enumerate(alphabet2):
            if el == letter:
                sentence3 += str(alphabet[x])
        if el == ' ':
            sentence3 += ' '
    return sentence3

sentence = input("Enter a sentence:\n")
number_rotation = input("Enter a rotation number: \n")

alphabet2 = rotate_alphabet(number_rotation)
cript_sentence = cripter(sentence, alphabet2)
decript_sentence = decripter(cript_sentence)

print(cript_sentence)
print(decript_sentence)