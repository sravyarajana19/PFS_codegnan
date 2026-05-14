print("operators")

'''
1.Arithmetic
+,=,*,%,/,//,**

ex:print(4%5 == 0)
print(2*3)
print(10**2)
print(10/2)
print(35.20//5)
-------------------
2.assignment
==,+=,-=,%=,*=

ex:count = 0
for j in range(1,10):
    count = count+1
print(count)   
-------------------
3.comparision
==,>=,<=,!=,<,>

ex:a = 7
b = 9
print(a == b)

--> == - looks for both the values equal or not
-------------------------------------------------
4.logical
and - both conditions must be true
or - atleast one condition must be true
not - opposition of the condition{false becames true ,true becames false }

ex:
a=5
if a%3 == 0 and a%15 == 0:
print("True")
if a%3 == 0 or a%5 == 0:
print("True")
print(not(5>2)) #flase
------------------------------
5.membership
in - present {exsists}
not in - not present{not exsisting]

ex:
fruits =["apple", "banana", "mango"]
print("apple" in fruits)     #true

fruits =["apple", "banana", "mango"]
print("orange" not in fruits)  #flase 
-------------------------------------
6.identity
is, is not
ex:
a=[1,2]
b=[1,2]
c=a
print(a is b)
print(id(a))
print(id(b))
print(a is c)

----> is = operator looks for the object is same or not
----------------------------------------------------------
7.bitwise
&- and{common}
| - or{combine}
^ - xor{different}
<< - leftshift {multiply by 2}
>> - rightshift {divide by 2}

ex:
print(5|3)
------------------------------
string - is sequence of char that are  enclosed in '', "", '''''' and string ios immutable

methodes:-
________
1.replace - used to replace with new substring.
syntax: - variable_name.replace("old","new")

ex:
any = "python is a lang"
print(any.replace("python","java"))
print(any)
--------------------
2.split - used to seperate into parts, and split based on the substring where before substring is one index and after is another index on the list.
syntax:
variable_name.split("substring")

ex:
any = "python is a lang"
print(any.split("is"))
print(any)
-------------------
3.len - get the number of items , substring
syntax:len(variable_name)

ex:
any = "python is a lang"
print(len(any))
---------------------
4.slicing - can give the access to get the particular index from the string
syntax:variable_name[starting index : ending index]

ex:
any = "python is a lang"
print(any[3:11})
--------------------
5.indexing - can accessing item using position numbers. python also supports neg indexing{neg start from end of the string}.
syntax:variable_name[indexing]

ex:
any = "python is a lang"
print(any.index("ang"))
---------------------
"substr".join(variable)
".".join(vari)

'''



