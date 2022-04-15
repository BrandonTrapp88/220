"""
Name: Brandon Trapp
Lab12.py

Problem: solving problems using while loops

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
from random import randint
def find_and_remove_first(list, value):
    ticker = 0
    while ticker < len(list):
        if value == list[ticker]:
            list.pop(ticker)
            list.insert(ticker,"brandon")
            value = None
        else:
            ticker+=1

def good_input():
    user_input = eval(input("Input a number betwee 1-10:"))
    while user_input < 1 or user_input > 10:
        if user_input < 1:
            print("Too low")
        elif user_input > 10:
            print("Too high")

        user_input = eval(input("Input a number betwee 1-10:"))
    else:return  user_input
def num_digits():

    user_input = eval(input("Enter a number, you may enter 0 or a negative number to exit"))
    blank_list = []
    answer = user_input

    ticker = 0
    while user_input != 0:

        while user_input != 0:
            user_input = user_input//10
            ticker+=1
        print(ticker)




def hi_lo_game():
    answer = randint(1,100)
    user_input = eval(input("Please guess a number between 1 and 100: "))
    guess = 1
    while guess <=7 and user_input != answer:
        if user_input > answer:
            print("You're too high")
        elif user_input < answer:
            print("You're too low")
        else:
            print("you're correct")
        user_input = eval(input("Please guess a new number: "))
        guess+=1
    print("the correct answer is ",answer)
