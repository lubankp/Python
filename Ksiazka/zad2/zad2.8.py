# Guess secret code

from random import randint


def guess_code(correct):
    corr = 0
    for x, el2 in enumerate(guess_number):
        find = 0

        for i, el in enumerate(random_code):
           # print (f"{el2}  {el}")
            if int(el) == int(el2):
                if i == x:
                    print(f"{el2} is in correct place")
                    find += 1
                    corr +=1
                    break
                else:
                    #print(f"g_num {guess_number.count(el2)} r_num {random_code.count(el)}")
                    if guess_number.count(el2) > random_code.count(el):
                        print(f"Too many {el2}")
                        find += 1
                    else:
                        print(f"{el2} is in not in correct place")
                        find += 1
                    break
        if find == 0:
            print(f"{el2} is in not in code")

    return corr


random_code = [randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)]

print(random_code)
correct = 0
while correct != 4:
    guess_number = input("Guess a code: \n")
    correct = guess_code(correct)

print("Congratulation!")
