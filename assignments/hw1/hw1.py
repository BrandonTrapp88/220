"""
Name: Brandon Trapp
hw1.py

Problem: 5 different functions that uses input() to figure out different problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""


def calc_rec_area():
    #ask user for the different mesurements
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    # area = length muliplied by the width
    area = length * width
    #post answer for the user
    print("Area = ",area)


def calc_volume():
    #ask user for the different mesurements
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    #calulation for the volume
    volume = length * width * height
    #post volume for the user
    print("The volume is ", volume)



def shooting_percentage():
    #ask user for the for the total shots taking and the total shots made
    total_Shots = eval(input("Enter the player total shots: "))
    shots_Made = eval(input("Enter how many shots the player made: "))
    #calculate the percentage and muliply that by 100 to covert the decimal to percetage.
    percentage = shots_Made / total_Shots
    new_Percentage = percentage * 100
    #display user shooting percentage
    print("Shooting percentage: ",new_Percentage,"%")




def coffee():
    #ask user for how many pounds of coffee
    pounds_coffee = eval(input("How many pounds of coffee do you want: "))
    #calculating the total cost of coffee
    coffee_cost = 10.50 * pounds_coffee
    shipping_cost = 0.86 * pounds_coffee
    fixed_cost = 1.50
    total_cost = coffee_cost + shipping_cost + fixed_cost
    #display total cost for user
    print("Your total is : $", total_cost)



def kilometers_to_miles():
    #ask user for how many kilometers they drove
    kilometers_Driven = eval(input("How many kilometers did you drive: "))
    #covert kilometers to miles
    covert = 1.61
    miles = kilometers_Driven / covert
    #display to miles to user
    print("you drove",miles, "miles ")




if __name__ == '__main__':
    pass
