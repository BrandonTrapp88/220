"""
Name: Brandon Trapp
hw11.py

Problem: solving problems using list

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
import math
class SalesPerson():
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def set_name(self,name):
        self.name = name

    def enter_sale(self,sale):
        self.sales.append(sale)

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        self.quota = quota
        if self.total_sales() >= self.quota:
            return True
        else:
            return False
    def compare_to(self, other):
        self.other = other
        if self.other > self.total_sales():
            return 1
        elif self.total_sales() > self.other:
            return 1
        else:
            return 0

    def __str__(self):
        statement = self.employee_id + "-"+self.name + ":" + self.total_sales()
        return statement

