"""
Name: Brandon Trapp
Lab10.py

Problem: Create a door and a button using classes

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
from graphics import*
class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(),label)

    def get_label(self):
        return self.text.getText()

    def set_label(self,label):
        return self.text.setText(label)

    def draw(self,win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self,point):
        self.point = point
        if (self.shape.getP1().getX() <= self.point.getX() <= self.shape.getP2().getX() and
            self.shape.getP1().getY() <= self.point.getY()<=self.shape.getP2().getY()):
            return True
        else:
            return False

    def color_button(self,color):
        self.shape.setfill(color)




