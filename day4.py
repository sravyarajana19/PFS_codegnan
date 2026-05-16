'''
Day 4 of my Python class.
----------------------------
String concatination:
--> The (+) symbol for integers can addition , but for other data types it will act as concatinating the data type
or values

Ex:
a = 70
b = 8
print(a+b)

any = "Python"
so = "is a language"
print(any + so)

an = [1,2]
am = [3,4]
print(an + am)
----------------------------------------------
Tuple:
--> Collection of different data types seperated by commas represented in "()" and immutable.

methods:
count()--> this is used to count the particular item in the tuple
index()--> this is used to know the index of the given tuple.

Ex:
some = (1,"Python",[1,2],(3,4))
print(some.index("Python"))
----------------------------------
Dictionary:
---> 'dict' is a key : value seprated by colon and both seprated by commas represented by "{}"

Methods:
keys(): Keys used to get all the keys from the dicitonary
syntax---> Variable.keys()

ex:
sravya_details = {"Name" : "sravya", 1 : 2 , (1,2) : [3,4]}
print(sravya_details.keys())
--------------------------------------

Values() : used to get all values from the dict.
syntax: Varaible.values()

EX:
sravya_details = {"Name" : "sravya", 1 : 2 , (1,2) : [3,4]}
print(sravya_details.values())
-------------------------------------

items() : used to get the key and value together.
syntax: dict:.items()
EX:
sravya_details = {"Name" : "sravya", 1 : 2 , (1,2) : [3,4]}
print(sravya_details.items())
-------------------------------------
update():
--> used to add a new key : value pair into dict
syntax: dict.update({key : value})

Ex:
sravya_details = {"Name" : "sravya", 1 : 2 , (1,2) : [3,4]}
sravya_details.update({"aadhar":"1235342345345535"})
print(sravya_details)
------------------------------------------
clear():
---> used to clear the all items in the dictionary.
syntax:
varaible_name.clear()
EX:
sravya_details = {"Name" : "sravya", 1 : 2 , (1,2) : [3,4]}
sravya_details.clear()
print(sravya_details)
'''

