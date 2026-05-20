'''
condition statments:
nested if, elif, if-else.


if: to check the stmt is true or false.

n = 40
if n % 2 == 0:
    print("even")
else:
    print("odd")
-----------------------
if-else:else in the if stmt, incase the condition becomes false then it will enter into fall-back(else), it will execute wtever inside it.

age = 13

if age >= 18:
    print("ur eligible for vote")
else:
    print(f" u have to wait for {18-age} more yrs")

-------------------------------------------------------------------------   
F-string:

n=79
if n%2==0:
    print(f"{n} is even num")
else:
    print(f"{n} is a odd num")   #nrmal ("odd") this will also print the ans.

    
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                        -----------practice coding que---------------
    
greater number:

num1 = 7
num2 = 15
if num1 >= 15:
    print(f"{num1} is greater then {num2}")
else:
    print(f"{num2} is greater then {num1}")
----------
leap year:

year = 2004
if(year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
    print("its a leap yr")
else:
    print("Not a leap yr")
-----------
vowels:

vowels = "b"
if vowels in "AEIOUaeiou":
    print(f"{vowels} is a vowel")
else:
    print(f"{vowels}is a consonent")
------------
+ve nd -ve:

num = -3
if num >= 0:
    print(f"{num} is +ve number")
else:
    print(f"{num} is -ve number")
-------------
students marks:

marks = int(input("enter ur marks: "))
name = input("enter ur name: ")
if marks >= 40:
    print(f"{name} is pass")
else:
    print(f"{name} is fail")
-------------
divisible or not:

num = 24
if num % 4== 0 and num % 6 == 0:
    print(f"{num} is div by 4 and 6")
else:
    print(f"{num} is not div by 4 and 6")
--------------
traffic lights:

c = int(input("enter \n1.red \n2.green:"))
if c == 1:
    print("stop")
else:
    print("go")
''' 
























    
