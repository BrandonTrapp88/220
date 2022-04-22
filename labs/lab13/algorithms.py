"""
Name: Brandon Trapp
Lab13.py

Problem: solving problems using while loops

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work

"""
import math
from graphics import *
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

def trade_alert(filename):
    file = open(filename, "r")
    blank_list = []
    line = file.readline()
    index = 0
    while line:
        blank_list = blank_list + line.split()
        line = file.readlines()
    for number in range(len(blank_list)):

        if int(blank_list[number]) > 830:
            print(number+1,"Warning")
        elif int(blank_list[number])==500:
            print(number+1,"ALERT")
    file.close()

def selection_sort(values):

    for number in range(len(values)):
        low = number
        for i in range(number+1 , len(values)):
            if values[i] < values[number]:
                low = i
        ticker = values[low]
        values[low] = values[number]
        values[number] = ticker

    return values

selection_sort([1,4,5,6,3,2,11,34])

def calc_area(rect):
    p1 = rect.getP1
    p2 = rect.getP2
    rec_width = math.fabs(p1.getX() - p2.getX())
    rec_height = math.fabs((p1.getY() - p2.getY()))
    area = rec_width * rec_height

    return area


def rec_sort(rectangles):
    for number in range(len(rectangles)):
        low = number
        for i in range(number+1 , len(rectangles)):
            if calc_area(rectangles[i]) < calc_area(rectangles[number]):
                low = i
        ticker = rectangles[low]
        rectangles[low] = rectangles[number]
        rectangles[number] = ticker

