"""
Name: Brandon Trapp
Lab12.py

Problem: solving problems using while loops

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
def read_data(filename):
    file = open(filename,"r")
    line = file.readline()

    num = 0
    blank_list = []
    while line:
        blank_list = blank_list + ((line.split()))
        line = file.readline()
        num+=1
    file.close()
    return blank_list


def is_in_linear(search_val, values):
    num = 0
    while num < len(values):
        if search_val == values[num]:

            return True
        num+=1

        return False

