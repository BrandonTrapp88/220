"""
Name: Brandon Trapp
hw5.py

Problem: Practice using different string methods

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def name_reverse():

    name = input("What is your name: ")
    name = name.split(" ")
    first = name[0]
    last = name[1]
    print(last+", "+first)

def company_name():

    name = input("Enter company name: ")
    name = name.split(".")
    comp_name = name[1]
    print(comp_name)

def initials():


    numb = eval(input("How many student names will you like to enter? "))


    for i in range(numb):
       names = input("Enter student name ")
       names = names.split(" ")
       first = str(names[0])
       last = str(names[1])
       print(first[0] + last[0])


def names():

    name = input("Enter a list of names: ")
    initals  = name.split(",")
    first = " "

    for i in initals:
        first = i.split()
        first_name = first[0]
        last_name = first[1]
        answer = first_name[0]+last_name[0]
        print(answer, end=" ")

def thirds():

    sent = eval(input("Enter number of sentences: "))
    blank_list =[]

    for i in range(sent):
        question = input("Enter your sentence: ")
        answer = question[0::3]
        blank_list.append(answer)
    for j in blank_list:
        print(j)

def word_average():
    sent = input("Enter a sentece: ")
    happy = sent.split()
    num = len(happy)
    word_count = 0
    for i in happy:
       word_count = word_count + len(i)
    print(word_count/num)


def pig_latin():

    sent = input("Enter a sentence: ")
    sent = sent.split()
    h1 = " "
    answer = " "




    for i in sent:
        letter = i[0]
        hi = h1+i[1:: ]

        answer =answer + ((hi.lower() + letter.lower() + "ay" ))
        answer= answer.lstrip()
    print(answer)







if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
