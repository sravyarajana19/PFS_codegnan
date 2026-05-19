'''
Type conversions
Changing one data type into another data type.

1. int():

an = 89
b = str(an)

an = 89
c=float(an)

an = "78"
b = int(an)
------------
int to str
int to float
float to int
str to float or int   #no when the string has numbers.
float str to float
float str in int #not directly posssible
-------------

| Data      | Meaning     |
| --------- | ----------- |
|  "10"     | text        |
|  10       | integer     |
|  "hello"  | word string |
|  10.5     | float       |
-----------------------------------

list:

any = [6,7]
print(str(any))
print(tuple(any))

tuple:
 
any = [6,7]
print(list(any))
print(str(any))

input:
------
a = int(input("enter ur num: "))
print(a)

str as a user i/p:
-----------------
s = input("enter a name: ")
print(s)

list as a user i/p:
-------------------
n = list(map(int,input("enter number:").split()))
print(n)

n = list(map(str,input("enter name:").split()))
print(n)

tuple as a user i/p:
--------------------
n = tuple(map(int,input("enter number:").split()))
print(n)

eval tells what type that word /number is :

n = eval(input("enter:"))
print(type(n))
'''


