"""
Name: Brandon Trapp
lab5.py

Problem: completing 6 functions using graphics.py. Also practiced with strings.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
from graphics import *
import math
def triange():
    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Draw a triangle", win_width, win_height)
    win.setBackground("white")

    #directions to draw shape
    inst_pt = Point(win_width / 2, win_height -10)
    inst_pt2 = Point(win_width / 2, win_height - 30)
    inst_pt3 = Point(win_width / 2, win_height - 50)
    instruction = Text(inst_pt, "Click three places to draw traiangle")
    instruction.draw(win)
    p1 = win.getMouse()
    p1.draw(win)

    p2 = win.getMouse()
    p2.draw(win)

    p3 = win.getMouse()
    p3.draw(win)

    side_a = math.sqrt(((p2.getX()-p1.getX())**2)+(p2.getY()-p1.getY())**2)
    side_b = math.sqrt(((p1.getX()-p3.getX())**2)+(p1.getY()-p3.getY())**2)
    side_c = math.sqrt(((p3.getX()-p2.getX())**2)+(p3.getY()-p2.getY())**2)

    perimeter = side_a + side_b + side_c
    side_s = perimeter/2
    area = math.fabs(math.sqrt(side_s * ((side_s-side_a)*(side_s-side_b)*(side_s-side_c))))
   

    tri = Polygon(p1,p2,p3)
    tri.setOutline("black")
    tri.setFill("red")
    tri.draw(win)
    per_answer = Text(inst_pt2, "The perimeter is: " + str(perimeter))
    per_answer.draw(win)
    area_answer = Text(inst_pt3, "The Area is: "+str(area))
    area_answer.draw(win)
    close_instruction = Text(inst_pt, "Click to close ")
    close_instruction.draw(win)
    instruction.undraw()


    win.getMouse()
    win.close()




def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    r_text_pt = red_text_pt.clone()
    r_text_pt.move(40, 0)
    r = Entry(r_text_pt, 4)
    r.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    g_text_pt = green_text_pt.clone()
    g_text_pt.move(40, 0)
    g = Entry(g_text_pt, 4)
    g.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    b_text_en = blue_text_pt.clone()
    b_text_en.move(40,0)
    b = Entry(b_text_en,4)
    b.draw(win)
    

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()
        red = eval(r.getText())
        green = eval(g.getText())
        blue = eval(b.getText())
        red = int(red)
        green = int(green)
        blue = int(blue)

        shape.setFill(color_rgb(red,green,blue))


    # Wait for another click to exit
    inst.undraw()
    close_msg = "Click to close window"
    inst = Text(Point(win_width / 2, win_height - 20), close_msg)
    inst.draw(win)
    win.getMouse()
    win.close()



def process_string():
    answer = input("input a string: ")
    print(answer[0])
    print(answer[-1])
    print(answer[2:6:])
    print(answer[0]+answer[-1])
    print(answer[0]*10)
    for i in (answer):
        print(i)

    print(len(answer))


def process_list():
    pt = Point(5,10)
    values = [5, "hi",2.5,"there",pt,"7.2"]
    x = values[1] + values[3]
    print((x))
    x = values[0]+values[2]
    print(x)
    x = values[1]
    print(x*5)
    x = list(values[2:5:])
    print(x)
    x = list(values[2:4])
    x.append(values[0])
    print(x)
    x = list(values[2:3:])
    x.append(values[0])
    x.append(float(values[5]))
    print(x)
    x = values[0] + values[2]+float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    terms = eval(input("Please Enter a number: "))

    answer = 0
    for i in range(terms):

        total = ( 2+(i % 3)*2)
        answer = answer + total
        print(total, end=" ")
    print()
    print("Sum is: ", answer)



def target():
    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")
    radius = 200
    list_colors = ["White","Black","Blue","Red","Yellow"]
    inst_pt = Point(win_width / 2, win_height - 10)
    for i in list_colors:

        cir = Circle(Point(200,200),radius)
        cir.draw(win)
        radius = radius - 30
        cir.setFill(i)

    instruction = Text(inst_pt, "Click to close")
    instruction.draw(win)

        
    win.getMouse()
    win.close()


