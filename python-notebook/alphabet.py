'''import string

def is_pangram(word):
    alphaset = set(string.ascii_lowercase)

    print(f'{alphaset}')
    print(f'{set(word.lower())}')
    return alphaset <= set(word.lower())

test_word = "The quick brown fox jumps over the lazy do!"

print(is_pangram(test_word))'''
from string import ascii_lowercase

def is_pangram(word):
    alphaset = set(ascii_lowercase)
    for letter in alphaset:
        if letter not in word.lower():
            return False
    return True

test_word = "The quick brown fox jumps over the lazy dog!"
print(is_pangram(test_word))
