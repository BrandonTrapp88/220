"""
Name: Brandon Trapp
lab1.py

Problem: getting the monthly percentage rate on the total credit card  balance for the month

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

def monthly_interest():
    annual_interest_rate = eval(input("What is your annual interest rate?: "))
    annual_interest_rate = annual_interest_rate / 100
    billing_cycle = eval(input("Days in billing cycle: "))
    previous_balance = eval(input("Previous Balance: $ "))
    payment = eval(input("Total amount you will like to pay:$ "))
    payment_date = eval(input("Day payment is made: "))

    avg_daily_balance = ((previous_balance * billing_cycle) - (payment*(billing_cycle-payment_date)))/ billing_cycle
    total_interest = (avg_daily_balance * (annual_interest_rate / 12))
    print("Your total interest for the month is: $", total_interest)

monthly_interest()
