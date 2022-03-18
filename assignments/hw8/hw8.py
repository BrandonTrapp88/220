"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
from graphics import *
import math

def add_ten(nums):

    x = nums
    new_list = []

    for i in x:
        answer = i +10
        new_list.append(answer)
    x.clear()
    for j in new_list:
        x.append(j)

def square_each(nums):

    x = nums
    new_list = []

    for i in x:
        answer = i*i
        new_list.append(answer)
    x.clear()
    for j in new_list:
        x.append(j)

def sum_list(nums):

   return sum(nums)

def to_numbers(nums):

    x = nums
    new_list = []

    for i in x:
        new_list.append(eval(i))
    x.clear()
    for j in new_list:
        x.append(j)

def sum_of_squares(nums):
    blank = []

    for i in nums:
        answer = i.split(",")
        to_numbers(answer)
        square_each(answer)
        answer = sum_list(answer)
        blank.append(answer)
    return blank

def starter(weight, wins):

    if weight >= 150 and weight < 160 and wins >= 5:
        return True
    elif weight > 199 or wins > 20:
        return True
    else:
        return False

def leap_year(year):
    pass


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("light red")
    circle_two.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    circle_one = circle_one.getCenter()
    circle_two = circle_two.getCenter()


if __name__ == '__main__':
    pass
