"""
Name: Brandon Trapp
Lab10.py

Problem: Create a door and a button using classes
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
from graphics import *

class Door:

    def __init__(self,shape, label):
        self.shape = shape
        self.label = Text(shape.getCenter(),label)

    def get_label(self):
        return self.label.getText()

    def is_clicked(self,point):
        self.point = point
        if (self.shape.getP1().getX() <= self.point.getX() <= self.shape.getP2().getX() and
            self.shape.getP1().getY() <= self.point.getY()<=self.shape.getP2().getY()):
            return True
        else:
            return False


    def set_label(self, label):
        self.label.setText(label)

    def draw(self,win):
        self.shape.draw(win)
        self.label.draw(win)
    def undraw(self):
        self.shape.undraw()
        self.label.undraw()
    def open(self,color, label):

        self.shape.setFill(color)
        self.label.setText(label)

    def close(self,color, label):
        self.shape.setFill(color)
        self.label.setText(label)
    def color_door(self,color):
        self.shape.setFill(color)
