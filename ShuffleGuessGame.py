from random import shuffle

""" 

>> There is a list containing two nulls and one 'O'. 
>> The list will be shuffled. 
>> The user will be asked to guess the position of 'O' by entering the index.

"""


def shuffle_list(list1: []):
    shuffle(list1)
    return list1


def user_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Enter your guess: 0,1, or 2: ")
    return int(guess)


def guess_check(list1, guess):
    if list1[guess] == 'O':
        print("Correct Answer!")
    else:
        print("Incorrect Answer!")
        print(list1)


myList = ['', 'O', '']
mixed_list = shuffle_list(myList)
guess = user_guess()
guess_check(mixed_list, guess)
