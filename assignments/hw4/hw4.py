"""
Name: Brandon Trapp
hw4.py

Problem: Solve issues using graphics.py

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
import math
from graphics import *



def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move circle")
    instructions.draw(win)

    # builds a square
    square = Rectangle(Point(100,100), Point(50,50))
    square.setOutline("red")
    square.draw(win)
    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = square.getCenter()# center of circle
        new_square =square.clone()
        new_square.draw(win)



        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        square.move(change_x, change_y)
    new_inst_pt = Point(width / 2, height - 200)
    new_instructions = Text(new_inst_pt, "Click to exit")
    new_instructions.draw(win)
    win.getMouse()



def rectangle():
    width = 400
    height = 400
    win = GraphWin("Draw a Rectangle", width,height)
    inst_pt = Point(width / 2, height - 10)
    instruction = Text(inst_pt, "Click two places to draw a rectangle.")
    instruction.draw(win)
    p1 = win.getMouse()

    p2 = win.getMouse()


    rec_width = math.fabs((p1.getX()-p2.getX()))
    rec_height = math.fabs((p1.getY()-p2.getY()))
    area = rec_width * rec_height
    per = 2*(rec_width+rec_height)


    rec = Rectangle(p1,p2)
    rec.setOutline("Red")
    rec.setFill("Red")
    rec.draw(win)
    instruction.undraw()
    area_answer = Text(inst_pt, "Area: " +str(area), )
    area_answer.draw(win)

    inst_pt2 = Point(width/2, height - 40)
    per_answer = Text(inst_pt2, "Perimeter: " +str(per))
    per_answer.draw(win)
    win.getMouse()






def circle():
    width = 400
    height = 400
    win = GraphWin("Draw a Circle", width, height)
    inst_pt = Point(width / 2, height - 10)
    instruction = Text(inst_pt, "Click to draw a circle")
    instruction.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    cirx = (p2.getX()-p1.getX())**2
    ciry =  (p2.getY()-p1.getY())**2

    radius = math.sqrt(cirx+ciry)
    cir_shape = Circle(p1, radius)
    cir_shape.draw(win)

    radius_answer = Text(inst_pt, "The Radius is: "+str(radius))
    instruction.undraw()
    radius_answer.draw(win)

    win.getMouse()








def pi2():
    #This problem is not complete.
    num = eval(input("Please enter the number"))
    answer = 0
    for i in range(1,num+1,2):
        answer = answer + (4/i - 4/(i + 2))
    print(answer)
pi2()





if __name__ == '__main__':
    pass
