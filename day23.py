'''
                                                                                File handling

file handler: is an object of file to maintain several function of the file like, creating , reading , updating and deleting the file.
-------------

open a file:
1. open()
>> name = open('filename','mode') 
>> name.close() -- for closing the file..
===================================
2. with open()

with open('filename','mode') as so:
    print(so.mode full form(''))
------------------------------------
modes:
 'r' -- used to read the file, error if file doesnot exsists....
 'a' -- used to add the text into file at last index , error if file doesnot exsists... === for this in code we use write in print insted of append.
 'w' -- used to add the txt into file but it will override of all txt inside file... if the file doesnot exsits it will create with that name.
 'x' -- used to create a file ...but will through error if we are used .
------------------------------------
method:

write()
read()
readline() -- can read only one line at a tym in a file...
readlines()

so = open('day23 demo.txt','r')
print(so.read())
so.close()

so = open('day23 demo.txt','w')
print(so.write('next is java'))
so.close()


so = open('demo.txt','x')
print(so.write())
so.close()

with open('demo.txt','w') as any_:
    any_.write('hello')



any_ = open('demo.txt','r')
print(any_.read(3))
any_.close()

any_ = open('demo.txt','r')
print(any_.readline(3))
any_.close()

any_ = open('demo.txt','r')
print(any_.readlines())
any_.close()

'''




































