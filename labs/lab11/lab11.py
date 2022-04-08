"""
Name: Brandon Trapp
Lab11.py

Problem: Create a 3 door game

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""

from graphics import *
from lab10.button import Button
from lab10.door import Door
from random import randint


def main():
    win_width = 400
    win_height = 400
    win = GraphWin("Three door game", win_width, win_height)
    win.setBackground("Blue")
    #exit
    p1 = Point(350, 30)
    p2 = Point(400, 100)
    #door
    p3 = Point(290, 180)
    p4 = Point(350, 350)
    #exit
    shape_1 = Rectangle(p1, p2)
    #winner score
    winning_lable = Text(Point(20,10), "wins")
    winning_lable.draw(win)
    winner = shape_1.clone()
    winner.move(-350, 0)
    score_1 = 0
    score = 0
    winner_score = Button(winner,score_1)
    winner_score.draw(win)

    #loser score
    loser_lable = Text(Point(80,10),"losses")
    loser_lable.draw(win)
    loser = winner.clone()
    loser.move(60,0)
    score_2 = 0
    loser_score = Button(loser, score_2)
    loser_score.draw(win)
    
    #exit button
    button = Button(shape_1, "Exit")
    button.draw(win)
    #doors
    shape_2 = Rectangle(p3, p4)
    shape_3 = shape_2.clone()
    shape_3.move(-150,0)
    shape_4 = shape_2.clone()
    shape_4.move(-280, 0)
    door_1 = Door(shape_2, "Door1")
    door_1.color_door("brown")
    door_1.draw(win)
    door_2 = Door(shape_3, "Door2")
    door_2.color_door("brown")
    door_2.draw(win)
    door_3 = Door(shape_4, "Door3")
    door_3.color_door("brown")
    door_3.draw(win)
    
    #instructions 
    
    game_instructions = Text(Point(230,50),"Click any door to guess the secret door")
    game_instructions.draw(win)

    number = randint(1,3)
    if number == 1:
        door_1.set_secret(True)
    else:
        door_1.set_secret(False)
    if number == 2:
        door_2.set_secret(True)
    else:
        door_2.set_secret(False)

    if number == 3:
        door_3.set_secret(True)
    else:
        door_3.set_secret(False)


    mouse_click = win.getMouse()


    while button.is_clicked(win.getMouse()) == False:

        if door_1.is_clicked(mouse_click) and door_1.is_secret():
            score_1 += 1
            winner_score.set_label(score_1)
            game_instructions.setText("Congrats you won")
            door_1.open("light green","Door 1")

        elif door_2.is_clicked(mouse_click) and door_2.is_secret():
            score_1 +=1
            winner_score.set_label(score_1)
            game_instructions.setText("Congrats you won")
            door_2.open("light green", "Door 2")
        elif door_3.is_clicked(mouse_click) and door_3.is_secret():
            score_1+=1
            winner_score.set_label(score_1)
            game_instructions.setText("Congrats you won")
            door_3.open("light green", "Door 3")
        else:
            if door_1.is_clicked(mouse_click):
                score_2 +=1
                loser_score.set_label(score_2)
                game_instructions.setText("Sorry you loss")
                door_1.close("red","Door1")
            elif door_2.is_clicked(mouse_click):
                score_2 +=1
                loser_score.set_label(score_2)
                game_instructions.setText("Sorry you loss")
                door_2.close("red","Door2")
            elif door_3.is_clicked(mouse_click):
                score_2+=1
                game_instructions.setText("Sorry you loss")
                loser_score.set_label(score_2)
                door_3.close("red","Door3")


    door_1.set_secret(False)
    door_2.set_secret(False)
    door_3.set_secret(False)










main()