"""
Name: Brandon Trapp
lab3.py

Problem: Creating a program that survey's the total amount of cars driven on a certain amount of roads.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
def department_of_transportation():
    total_vehicles = 0
    total_roads = eval(input("How many roads were surveyed: "))
    #starting for loops to get the calculations of the cars on road on certain days.
    for i in range(1,total_roads+1):
        print("How many days was road ", i,"surveyed", end= " ")
        days = eval(input())
        average = 0
        for j in range(1,days+1):
            print("\t how many cars travel day",j, end=" ")
            cars = eval(input())
            total_vehicles = cars + total_vehicles
            average = cars + average
        print("Road",j,"average vehicles per day: ", average/days)
    print("Total number vehicles traveled for all roads:", total_vehicles)
    print("Total average for all roads: ", total_vehicles/total_roads)
