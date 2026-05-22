'''
Nested loop: loop inside loop .

ex:
for i in range(1,10):
    for j in range(1,2):
        print(i)
        print(j)
 ----------------------------   
table:

num =5

for i in range(1,11):
    print(f"{num} x {i} = {i*num}")
-----------------------------
reverse the string:

so = "sravya"
emp_str = ""
for i in so:
    emp_str = i+emp_str
    print(emp_str)
if emp_str == so:
    print(f"{so} is a palindrome")
else:
    print(f"{so} is not a palindrome")
----------------------------
armstrong num:

num = int(input("enter a number: "))
arm = 0
so = len(str(num))

for i in str(num):
    arm = arm + int(i) ** so

if arm == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

-----------------------------
perfect num:
  
num = int(input("enter a num:"))
perf_num = 0
for i in range(1,num):
    if num % i == 0:
        perf_num += i
if perf_num == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")
---------------------------------
prime numbers:
    
   
num = int(input("enter a num:"))
count = 0
for s in range(1,num+1):
    if num % s == 0:
        count += 1
if count == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
-----------------------------------
pattern:
       
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")  #a,ab,abc,abcd
    print()    

n = 5
count = 0
for i in range(1,n+1):
    for j in range(1,i+1):       #1,12,123,1234 if we give j in print insted of count
        count += 1
        print(count,end=" ")
    print()    
------------------------------------
reverse pattern:

n = 5
count = 0
for i in range(n,0,-1):
    for j in range(1,i+1):       
        count += 1
        print("*",end=" ")
    print()    
----------------------------------
pyramid:

n = 5
for j in range(1,n+1):
    print(" "*(n-j), end="")
    for i in range(1,j+1):
        print("*",end=" ")
    print()    



n = 5
for j in range(n,0,-1):
    print(" "*(n-j), end="")
    for i in range(1,j+1):
        print("*",end=" ")
    print() 


n = 5
for j in range(n,0,-1):
    print(" "*(n-j), end=" ")
    for i in range(j):
        print("*",end=" ")
    print() 

'''















    

    
