'''
project based on Regex:
========================

validation:

1. mobile number --> 10 digits

2.password --> cap, small, digit, speciLal char, atleast 8

3.mail --> @gmail.com
-------------------------


import re

class Validation:
    def __init__(self, mobile, email, password):
        self.mobile = mobile
        self.email = email
        self.password = password

    def v_mobile(self):
        return re.match("^[6-9][0-9]{9}$", self.mobile)
    
    def v_password(self):
        return re.match("^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$", self.password)
    
    def v_email(self):
        return re.match("^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", self.email)

    def display(self):
        if self.v_mobile():
            print("Valid Mobile")
        else:
            print("Invalid Mobile")

        if self.v_email():
            print("Valid Email")
        else:
            print("Invalid Email")

        if self.v_password():
            print("Strong Password")
        else:
            print("Weak Password")

mobile = input("Enter Mobile Number: ")
email = input("Enter Email: ")
password = input("Enter Password: ")

u = Validation(mobile, email, password)
u.display()

'''










































