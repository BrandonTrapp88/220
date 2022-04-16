from sales_person import SalesPerson
"""
Name: Brandon Trapp
hw11.py

Problem: solving problems lists

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
class SalesForce():

    def __init__(self):
        self.sales_people = []

    def add_data(self,file_name):
        self.file_name = file_name
        file = open(self.file_name,"r")
        for i in file.readlines():
            i = i.split(",")
            self.sales_people.append(i)

    def quota_report(self, quota):
        pass


    def get_sale_frequencies(self):
        pass