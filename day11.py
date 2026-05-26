'''
assert: {this is debugging statement used to test whether a condition is true}

assert is used to check whether a condition is True or False.

If condition is True → program continues
If condition is False → program stops with error

ex:
num = 11
assert num > 10
print("True")
-------------------
functions:
A function is a block of code which only execute when it is called .
You can pass data known as parameters into a function.
To avoid repeated lines in code.

def means >>> defining function
func() >>> Function call.
paraneters >>> inputs.

Why Functions are Used

✅ Reuse code
✅ Avoid repetition
✅ Easy debugging
✅ Cleaner programs

Function = reusable code block

-----------
def function_name(parameters):
    ------------
    code-------
    -----------
function_name(arguments)
-----------
def greet():
    print("Hello")
----------
num = 9
def even(num):
    prin(num)
even(num)    
 ------- 
num = 9
def even(num):
    if num % 2 == 0:
        print("even")
    else:
        print(f"{num} odd")
even(num)  
even(109)
-----------------------------
ways to pass arguments:
    1. required  arguments: a function must be called with the same no of arguments

ex:
    
def even(num,num2):
    if num % 2 == 0:
        print("even")
    else:
        print(f"{num} odd") 
even(109,90)
--------------------------
    2. default arguments:by default, values is defined at parameters even tho it takes from arguments.

ex:

def even (name = "srav", age = 22, sal = 10):
     print(name,age,sal)
even("sravya",22,80000)
---------------------------------
   3. key word arguments: we can send arguments with key =  value syntax. by this , the order of arguments does not matter.
   
ex:
def even (age,sal,name):
    pringt(name , sal , age)
even(name = "srav",age = 78,sal = 80000)
-------------------------------
   4. variable length arguments: adding a star(*) before the parameter name in the function, receive a tuple of arguments and can access items with indexes.

ex:

def even (*name):
    print(name[2])
even("abc","def","ghi","jkl")
-------------------
name = "srav"
def even(any):
    print(any)
even(name)    
'''





















   

















    
