"""
Name: Brandon Trapp
lab2.py

Problem: getting numbers from a user and giving 3 different mean outputs back to the user.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
import math
def means():
    #accumlator vars
    rms = 0
    harmonic_mean = 0
    geometric_mean = 1
    #number of submissions we're getting from the user
    number_of_submissions = eval(input("Enter how many numbers you will like to enter: "))
    #for loop that goes through the number of submissions storing the values
    for i in range(number_of_submissions):
        numbers = eval(input("Enter a number: "))
        rms = (numbers**2) + rms
        harmonic_mean = (1/numbers)+ harmonic_mean
        geometric_mean = numbers * geometric_mean
    root_mean_square_answer = math.sqrt(rms/number_of_submissions)
    harmonic_mean_answer = number_of_submissions / harmonic_mean
    geometric_mean_answer = geometric_mean ** (1/number_of_submissions)
    #display to the user their answer
    print("Your Root-Mean-Square answer is: ", root_mean_square_answer)
    print("Your harmonic mean answer is: ", harmonic_mean_answer)
    print("Your Geometric Mean answer is: ", geometric_mean_answer)
