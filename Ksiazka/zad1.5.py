from random import randint

def guess_number():
    number = randint(1, 100)
    guess_number = int(input("Guess a number: \n"))
    while guess_number != number:
        if guess_number > number:
            print("Lower!")

        else:
            print("Higher!")

        guess_number = int(input())
    print("Congratulation!")

guess_number()
