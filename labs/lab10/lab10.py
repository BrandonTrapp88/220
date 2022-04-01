"""
Name: Brandon Trapp
Lab10.py

Problem: Create a gui that encodes a message from the user based on a key and display the answer

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
from graphics import *
from button import Button
from door import Door
def main():
    win_width = 400
    win_height = 400
    win = GraphWin("Test", win_width, win_height)
    win.setBackground("Light Gray")

    p1 = Point(100,30)
    p2 = Point(300,100)
    p3 = Point(140,150)
    p4 = Point(250,350)

    shape_1 = Rectangle(p1, p2)
    #shape_1.draw(win)
    
    shape_2 = Rectangle(p3,p4)


    button = Button(shape_1,"Exit")
    button.draw(win)

    door = Door(shape_2,"Close")
    door.draw(win)
    x = "green"
    y = "red"

    while door.is_clicked(win.getMouse())== True:
        if door.is_clicked(win.getMouse()):
            door.open(x,"Open")
        if door.is_clicked(win.getMouse()):
            door.close(y,"Close")
        if button.is_clicked(win.getMouse()):
            win.close()
            break





main()
