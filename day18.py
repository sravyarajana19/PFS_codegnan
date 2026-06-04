'''
oops: {object oriented programing system}
============================================

--------------------------------------------------------------------
1. class : a class is a blueprint or a template used to create object.


class stu_:
    def edu_(self):
        print("i am studying btech")
    def sports(self):
        print("cricket")
        print("vallyball")
s1 = stu_()
s1.edu_()
s1.sports()
    

-----------------------------------------------------------------------
2.object : an object is an instance of a class


class stu_:
    name = "sravya"

s1 = stu_()
print(s1.name)

-------------------------------------------------------------------------------
attributes: these are variables that are belongs to class or an object.


class stu_:
    name = "sravya"
    age = 22

s1 = stu_()
print(s1.name)
print(s1.age)
-------------------------------------------------------------------------------------------
methods: the functions defined inside the class is called methods.


class PFS_DA:
    def python(self):
       PFS_DA = 'batch_03'
       print('this is PFS and DA batch03')
       
    def Flask(self):
        PFS = 'batch_03'
        print("this is PFS batch 03")

all_ = PFS_DA()
all_.python()
all_.Flask()
----------------------------------------------------------------------------------------
constructor :{__init__}

class ATM:
    def __init__(self,balance,name):
        self.balance =balance
        self.name = name
    def bal_check(self):
        print(f"{self.name} your total balance is {self.balance + 7000}")
    def name_(self):
        print(self.name)

card = ATM(balance = 5000,name = "sravya")
card.bal_check()
card.name_()
------------------------------------------------------------------------------------------------------------

Access specifiers:

1.public : this can be accessed from anywhere in the program .(sravya)

eg:
class stu:
    __name = "sravya"

s1 = stu()
print(s1._stu__name)

------------------------
2.protected :  this is represented using a single underscore.(_)

-----------------------
3.private : this is represented using a double underscore.(__)


--------------------------------------------------------------------------------------------------------------

Encapsulation : is the process of binding data and methods together.


class bank:
    def __init__(self,balance):
        self.__balance = balance


    def depo_(self , amount):
        self.__balance += amount

    def get_bala(self):
        return self.__balance

acc = bank(1000)
acc.depo_(60000000)
print(acc.get_bala())

'''




























        
