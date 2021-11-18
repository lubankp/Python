# chapter 8 - when things go wrong

# sample 1:
import random


def safe_lookup(d,k):
    try:
        return d[k]
    except KeyError:
        print(f'Could not find value for key {k}')
        return -1

safe_lookup({1: 'one', 2: 'two', 3: 'three'}, 0)

# sample 2:
# def add3(x,y):
#   return x+y+z

# print(add3(1,2))

# sample 3:

def repeated(e, length):
    try:
        if length < 0 : raise ValueError
        l = []
        for x in range(0,length): l.append(e)
        return l
    except ValueError:
        print("This is Value Error")

print(repeated(1, -1))

# sample 4:

def safe_lookup1(d, k):
    try:
        print('attempting key lookup')
        result = d[k]
    except Exception as e:
        print('Unknown error in safe_lookup')
        raise e
    else:
        print('key lookup succeeded')
        return result

safe_lookup1({1: 'one', 2: 'two', 3: 'three'}, 1)

# sample 5:

from random import randint

def get_guess(message):
    try:
        this_guess = int(input(message))
    except ValueError:
        print('Not a number!')
        return get_guess('')
    else:
        if this_guess < 1 or this_guess > 100:
            print('Number not in range 1-100')
            return get_guess('')
        return this_guess

def guessing_game():
    target = random.randint(1,100)
    guess = get_guess('Guess a number between 1 and 100\n')
    tries = 1
    while guess != target:
        tries += 1
        if guess < target:
            guess = get_guess('Higher!\n')
        elif guess > target:
            guess = get_guess('Lower!\n')
    print(f'Congratulation! You took {tries} guesses')

guessing_game()