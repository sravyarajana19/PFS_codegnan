'''
Inheritance: this allows one class to aquire the properties and methods of another class .

types:
1. single inheritance : a class inherits from a single parent class is called singel inheritance.

class father:
    def land(self):
        print("My father have 5A")
        
class sravya(father):
    def my_own(self):
        print(" i have 2 A")

fam = sravya()

fam.land()
--------------------------

2. multiple inheritance : a child inherits from more than one parent class


class father:
    def land(self):
        print("My father have 5A")

class mother:
    def gold(self):
        print("my mother have 1kg G")
        
class sravya(father,mother):
    def my_own(self):
        print(" i have 2 A")

all_ = sravya()
all_.land()
all_.gold()
---------------------------
3. multi -level inheritance : a class inherits from a parent  class and another class inherits from that child class .


class grandfather:
    def land(self):
        print("my grandfather have 5acres of land")

class father(grandfather):
    def flat(self):
        print("my father owns a flat at banglore")

class son(father):
    def ntg(self):
        print("i own their properties")

all_ = son()
all_.land()
all_.flat()
all_.ntg()
----------------------------
4. hierarchical inheritance : multiple child class inherit from a singel parent.


class father :
    def land(self):
        print("10 a land")

class sravya(father):
    def mine(self):
        print("job")

class sri(father):
    def sis(self):
        print("studying")

s1 = sri()
s1.land()

s2 = sravya()
s2.land()
---------------------------
5. hybride inheritance: this is tha combination of two or more types of inheritance.

class A:
    def so (self):
        print("class A")
class B:
    def why (self):
        print("class B")

class C:
    def any (self):
        print("class C")
        
class D(B,C):
    def to (self):
        print("class D")

how = D()
how.any()

------------------------
SUPER METHOD: this is used to access methods and constructor of the parent class from the child class.

class parent:
    def display(self):
        print("method parent")

class child(parent):
    def display(self):
        super().display()
        print("method child")
        
all_ = child()
all_.display()

-------------------------------
class person:
    def __init__(self,name):
        self.name = name
class stu_(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll

    def show(self):
        print(f"Name : {self.name}")
        print(f"Roll no : {self.roll}")

any_ = stu_("sravya",107)
any_.show()

'''















        



















