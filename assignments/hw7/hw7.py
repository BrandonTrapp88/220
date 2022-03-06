"""
Name: brandon trapp
hw7.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""

def number_words(in_file_name, out_file_name):

    lines = open(in_file_name, "r")
    words =lines.readlines()
    lines.close()
    output = open(out_file_name, "w")
    number = 1

    for i in (words):
        x = i.split()
        for j in range(len(x)):
            blank= (str(number)+ " "+str(x[j]))
            print(blank, file=output)
            number = number+1

def hourly_wages(in_file_name, out_file_name):

    infile = open(in_file_name,"r")
    employee = infile.readlines()
    infile.close()
    output = open(out_file_name, "w")
    total = 0
    for i in range(len(employee)):
        person = employee[i].split()
        pay = person[2]
        hours = person[3]
        total = total+ ((float(pay) * int(hours))+ (int(hours) * 1.65))
        answer = person[0]+" "+person[1]+" "+"{:.2f}".format(total)
        total = 0
        print(answer,file=output)

def calc_check_sum(isbn):
    pass





def send_message(file_name, friend_name):
    file = open(file_name,"r")
    friend = open(friend_name+".txt","w")
    for i in(file):
        print(i, end="", file=friend)


def encode():
    pass


def send_safe_message(file_name, friend_name, key):
    pass


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    pass
