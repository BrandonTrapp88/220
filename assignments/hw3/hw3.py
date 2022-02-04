"""
Name: Brandon Trapp
hw3.py

Problem: Solving different problems with for loops.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def average():
    grade= 0
    total_grades = eval(input("How many grades will you like to enter: "))
    for i in range(total_grades):
        grade_request = eval(input("Enter grade: "))
        grade = grade + grade_request
    answer = grade/ total_grades
    print("Your grade is: ", answer)


def tip_jar():
    total_tip = 0
    for i in range(5):
        tip_request = eval(input("How much would you like to tip: "))
        total_tip = tip_request + total_tip
    print("Your tip amount is: ", total_tip)



def newton():
    square = eval(input("What number will you like to square: "))
    approx = eval(input("How many times should we apporve the  approximation: "))
    start = square
    for i in range(1,approx+1):
        start = (start + (square/start))/2
    print(start)




def sequence():
    numbers = eval(input("how many terms would you like: "))
    for i in range(1,numbers+1):
        print(i+(i%2)-1)






def pi():
    number_terms = eval(input("How many terms in the series: "))
    answer = 1
    for i in range(number_terms):
        pi_math = (i+2-(i%2))/(i+1+(i%2))
        answer = answer * pi_math
    answer = answer*2
    print(answer)

if __name__ == '__main__':
    pass
