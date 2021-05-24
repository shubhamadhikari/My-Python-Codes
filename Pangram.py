"""
A Pangram is a word or a sentence containing all English alphabets at least once.

"""

import string


def check_pangram(myString):
    myString = myString.replace(' ', '')
    myString = myString.lower()
    alpha = string.ascii_lowercase
    for x in alpha:
        if x not in myString:
            print(x)
            return False
    return True


print(check_pangram('The quick brown fox jumps over the lazy dog'))
