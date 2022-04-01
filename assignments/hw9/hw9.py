"""
Name: brandon trapp
hw9.py

Problem: Create a hangman game.
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
import random
from random import randint

def get_words(file_name):

    file = open(file_name, "r")
    words = file.readlines()
    return words

def get_random_word(words):

    random_index = random.randint(0, len(words) - 1)
    answer = words[random_index]
    return answer.rstrip()

def letter_in_secret_word(letter, secret_word):

    if letter in secret_word:
        return True
    else:
        return False

def already_guessed(letter, guesses):

    if letter in guesses:
        return True
    else:
        return False

def make_hidden_secret(secret_word, guesses):

    blank_string = "_" * len(secret_word)
    blank_list = list(blank_string)
    for i in guesses:
        for j in range(len(secret_word)):
            if secret_word[j]==i:
                blank_list[j] = i
    return " ".join(blank_list)

def won(guessed):
    for i in guessed:
        if i == "_":
            return False
    return True

def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    pass


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
