'''
Build - in function:

print()
input()
len()
type()
max()
min()
----------------------
sort() and sorted(): both are used for arrange in order.

>Creates new sorted list
Original stays same
Works with list, tuple, string

m = [3,4,6,1,2]
print(sorted(m))
print(m)


> Changes original list
Works only for lists

m = [3,4,6,1,2]
m.sort()
print(m)

------------------
recursive function:
 a recursive function that calls itself to solve a problem by breaking it into small or simple sud- pblm.

def fuc(num):
    if num == 1:
        return 1
    return num*fuc(num-1)
print(fuc(8))
---------------------

def even(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
even(4)


------------------

def add(a,b):
    return a+b
res = add(4,4)
print(res)


lambda function/anonyamous/:
A lambda function is a small anonymous function.

Anonymous means:
function without normal name using def.

syntax:
lambda arguments: expression

so = lambda a,b,c:a+b+c+a
print(so(4,5))

num = lambda a: a*a
print(num(5))

s = lambda a,b:a-b
print(s(5,3))


n = lambda a,b:a%b
print(n(2,4))


n = lambda a,b:a/b
print(n(2,8))

































