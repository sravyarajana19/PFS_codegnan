'''
fabinoucci series:

a = 0
b = 1
def fab(a,b):
    for i in range(1,n):
        c = a + b
        a = b
        b = c
        print(c,end=" ")
n = int(input("enter the limit:"))
print(a,b,end=" ")
fab(a,b)
-------------------------------------------
remove duplicate in list:

n = [2,5,7,9,2,7]
a = []
def dup(n,a):
    for i in n:
        if i not in a:
            a.append(i)

    print(a)
dup(n,a)    
---------------------------------------
no.of words in a string:

count = 0
a ="Discover Python's versatility, from web development to data analysis".split()
def lett(a,count):
    for i in a:
        count += 1
    print(count)
lett(a,count)    
 '''   
    
