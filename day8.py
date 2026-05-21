'''any = [1,2,"python",[3,4,["java",5],[6,["programming",7],8],([9,10],"someone"),"i am doing well"],(11,12)]

print(any[3][4][0])      
------------------------------------------------------------------------------------------------------------------------------------------------       
elif:


marks = 95

if marks>=90:
    print("A+")
elif marks>=80:
    print("A")
elif marks>=70:
    print("B+")
elif marks>=60:
    print("B")
elif marks>=50:
    print("C+")
elif marks>=35:
    print("Pass")
else:
    print("Fail")
    
----------------------    
 max out of three ?   

a = 5
b = 9
c = 7
if a > b and a > c :
    print("a")
elif b > a and b >  c:
    print("b")
else:
    print("c")
-----------------------
nested-if:


SBI_bank = {"ATM PIN":"2619"}
pin = input("Enter 4 digit ATM pin: ")
if len(pin) ==4:
    if pin in SBI_bank["ATM PIN"]:
        print("Welcome to sbi bank")
    else:
        print("Invalid")
else:
    print("pls enter 4 digit number")
------------------------
for loop:

ex:
any = "python"
an = [1,2,3,4,5]
so = [6,3,4,8,9]
for n in any:
    print(n)
-------------------    
range: isn a inbuild function used to generate numbers in sequence manner

syntax: range(start,end,step)

ex:
for i in range(1,10,3):
    print(i)
else:
    print("code ended here")

else in for:once the itteration completed this else will be executed.    
-------------------
break:
 used to exit from the loop based on the condition.

 ex:
for i in range(1,10):
     print(i)

     if i == 5:
         break    

------------------
continue:
    used to skip the current itteration if the condition is matched

ex:    
for i in range(3,9):
    
    if i==6:
        continue
    print(i)
-----------------------
pass: null statment it means it do no changes.

for i in range(4,9):

    if i ==6:
        pass
    print(i)
-----------------------
while loop: while is a combination of for and if stmt.

ex:

i = 1
while i < 6:
    print(i)
    i += 1

--------------------------------------------------------------------------------------------------------------------------------    
    
























    
