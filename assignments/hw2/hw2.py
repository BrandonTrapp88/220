"""
Name: Brandon Trapp
hw2.py

Problem: creating different functions using import math

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
import math


def sum_of_threes():
    #setting a variable of sum  to 0. This stores my numbers in my for loop
    total = 0
    #gets the upper bound number from user.
    upper_bound = eval(input("Enter the upper bound number: "))
    #loop that goes through the upperbound, starting at the number 3 by 3's
    for i in range(3,upper_bound+1,3):
        total = i+total
    print("sum of threes is: ", total)



def multiplication_table():
    #using a for loop to print out the table
    for i in range(1,11):
        print()
        for j in range(1,11):
            #multiplying the numbers to get the other totals
            lines = i * j
            print(lines, end=" \t")




def triangle_area():
    #getting the measurements for the sides of the triangle
    side_a = eval(input("Enter a value for side a: "))
    side_b = eval(input("Enter a value for side b: "))
    side_c = eval(input("Enter a value for side c: "))
    #the formula for getting the area of a triangle
    square_s = (side_a+side_b+side_c)/2
    total_square = (square_s*((square_s-side_a)*(square_s-side_b)*(square_s-side_c)))
    print("The area of your triangle is ", math.sqrt(total_square))


def sum_squares():
    #getting the numbers from user to square
    lower_range = eval(input("Enter the lower range: "))
    upper_range = eval(input("Enter the upper range: "))
    total = 0
    #going through the variables storing the answer in the sum variable
    for i in range(lower_range, upper_range+1):
        total = (i * i ) + total
    print(total)



def power():
    #getting the base and exponent from the user.
    base = eval(input("Enter the base: "))
    exponent = eval(input("Enter the exponent: "))
    answer = 1
    #creating the answer
    for i in range(exponent):
        answer = (base * answer)
    #displaying the answer
    print(base,"^", exponent, " = ", answer)


if __name__ == '__main__':
    pass
