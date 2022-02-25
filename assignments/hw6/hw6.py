"""
Name: Brandon Trapp
hw6.py

Problem: Solve different functions using format, and return

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""

import math

def cash_converter():

   cash = eval(input("Enter a number: "))
   answer = ("That is ${:.2f}dollars.".format(cash))
   print(answer)


def encode():
    sentence = input("Please Enter a sentence: ")
    key = eval(input("Enter a key: "))
    answer = ""

    for i in sentence:
        new_sentence2 =ord(i)+ key
        answer = answer +chr(new_sentence2)
    print(answer)





def sphere_area(radius: float):
    
    area = 4*((radius**2)*math.pi)
    return area



def sphere_volume(radius):
    volume = 4/3 * (math.pi * (radius**3))
    return volume


def sum_n(number):
    answer = 0
    for i in range(1,number+1):
        answer = answer+i
    return (answer)


def sum_n_cubes(number):
    answer = 0
    for i in range(1,number+1):
        answer = answer + (i**3)
    return answer


def encode_better():
    sentence = input("Enter a sentence: ")
    key = input("Enter a key: ")

    answer = ""

    for i in range(len(sentence)):
        message = ord(sentence[i]) - 65
        new_key = ord(key[i % len(key)]) - 65
        new_message = (message+new_key) % 58
        new_message = new_message +65
        answer = answer+chr(new_message)
    print(answer)








        






if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
