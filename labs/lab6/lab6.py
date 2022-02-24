"""
Name: Brandon Trapp
Lab6.py

Problem: Create a gui that encodes a message from the user based on a key and display the answer

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
from graphics import *
def vigenere():
    #create window
    win_width = 400
    win_height = 400
    win = GraphWin("Vigenere", win_width, win_height)
    win.setBackground("Light Gray")
    
    #create instructions for entry boxes
    inst_pt = Point(win_width/6,win_height-300)
    instructions1 = Text(inst_pt, "Message to Code: ")
    instructions1.draw(win)

    inst_pt2 = Point(win_width / 6, win_height - 250)
    instructions2 = Text(inst_pt2, "Enter Keyword: ")
    instructions2.draw(win)


    #create entry box
    inst_pt3 = Point(win_width-200, win_height - 250)
    user_entry = Entry(inst_pt3, width=20)
    user_entry.draw(win)
    
    inst_pt4 = Point(win_width-170, win_height - 300)
    user_entry_2 = Entry(inst_pt4, width=30)
    user_entry_2.draw(win)

    #Create Buttton
    button = Rectangle(Point(150,200),Point(250,240))
    button_instruction = Text(button.getCenter(), "Encode")
    button_instruction.draw(win)
    button.draw(win)
    win.getMouse()


    #variables for messages
    message = user_entry_2.getText().upper().replace(",","")
    key = user_entry.getText().upper().replace(",","")
    answer = " "

    #loop through message
    for i in range(len(message)):
        message_cap = ord(message[i])-65
        new_key = ord(key[i % len(key)])-65
        capital = (message_cap + new_key) % 26
        new_capital = capital + 65
        answer = answer +chr(new_capital)

    #display answer
    answer_display = Text(button.getCenter(), "Resulting message is \n"+str(answer))
    answer_display.setSize(10)
    button.undraw()
    button_instruction.undraw()
    answer_display.draw(win)

    #closing instructions

    inst_pt5 = Point(win_width/2,win_height-10)
    closing_instructions = Text(inst_pt5,"Click Anywhere to Close Window")
    closing_instructions.draw(win)

    win.getMouse()
    win.close()




