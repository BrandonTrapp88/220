from graphics import *
def greeting_card():
    width = 400
    height = 400
    win = GraphWin("Happy Valentines Day" , width, height)
    win.setBackground("pink")
    inst_pt2 = Point(width / 2, height - 380)
    valentines = Text(inst_pt2, "Happy Valentines Day " )
    valentines.setSize(30)
    valentines.draw(win)


    center = Point(200,220)
    center2 = Point(260,220)
    p1 = Circle(center,30)
    p1.setFill("red")
    p1.setOutline("red")
    p2 = Circle(center2, 30)
    p2.setFill("red")
    p2.setOutline("red")
    p3 = Polygon(Point(170,225), Point(290,225),Point(230,300))
    p3.setFill("red")
    p3.setOutline("red")
    p3.draw(win)
    p2.draw(win)
    p1.draw(win)
    arrow = Line(Point(10,256), Point(60,256))
    arrow_point = Polygon(Point(60,260),Point(60,250),Point(80,250))
    arrow_point.draw(win)
    arrow.draw(win)

    for i in range(10):
        arrow.move(50,0)
        arrow_point.move(50,0)
        time.sleep(1)
    win.close()
