"""
Name: Brandon Trapp
lab8.py

Problem: completing a bumper car program

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import *
import math

def get_random(move_amount):
    return randint(-move_amount,move_amount)
def did_collide(ball, ball2):
    ball_x = ball.getCenter().getX()
    ball2_x = ball2.getCenter().getX()
    ball_y = ball.getCenter().getY()
    ball2_y = ball2.getCenter().getY()
    
    distance = math.sqrt(((ball2_x - ball_x)**2) + ((ball2_y - ball_y)**2))
    radius = math.sqrt(ball_x + ball_y)
    if distance >= radius:
        return True
    else:
        return False

def hit_verical(ball, win):
    ball_y = ball.getCenter().getY()
    if ball_y >= 360:
        return True
    elif ball_y <= 40:
        return True
    else:
        return False
def hit_horizontal(ball, win):
    ball_x = ball.getCenter().getX()

    if ball_x >= 360:
        return True
    elif ball_x <= 40:
        return True
    else:
        return False

def get_random_color():
    shape_color = color_rgb(randint(0,255), randint(0,255), randint(0,255))
    return shape_color



def bumper():
    width = 400
    height = 400
    win = GraphWin("Bumper Cars", width, height)
    p1 = Point(randint(0,390),randint(0,390))
    p2 = Point(randint(0,390),randint(0,390))
    ball = Circle(p1, radius=40)
    ball.setFill(get_random_color())
    ball2 = Circle(p2, radius=40)
    ball2.setFill(get_random_color())
    ball.draw(win)
    ball2.draw(win)
    while win.checkMouse() == None:
        ball.move(get_random(10),10)
        time.sleep(0.1)

        
    win.getMouse()
    

    

       
        


    

bumper()

