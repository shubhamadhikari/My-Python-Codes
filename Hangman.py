import random
import string

from words import words


def get_valid_word(w):
    word = random.choice(w)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(w)

    return word


def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives != 0:
        # letter used
        print("You have", lives, "lives left and you have used these letters: ", ' '.join(used_letters))

        # what current word is [W - R D]
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current Word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1  # take one life away if guess is wrong
                print("The letter is not present in the word.")

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the word", word, "!!")


hangman()
