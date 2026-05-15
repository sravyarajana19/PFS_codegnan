print("hello")
'''
syntax:
  v ariable_name[index position]
  ".".join(vari)

any = "p.y.t.h.o.n. .i.s. .a. .l.a.n.g.u.a.g.e."
print(any[7])
print(any.index("ang")

1. prgm to convert 24h clock into nrml clock?
'''
time_="20:37"
parts_=time_.split(":")
hour_=int(parts_[0])
min_=int(parts_[1])
print(f"{time_} is converted into {hour_ - 12}:{min_} pm")

'''
--> list: list is a collection of diff data types .
it is represented in [] (sqaure brackets) and seperated by , (commas).
index starts from 0.
list are mutable --can change values.

ex:
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
print(fruits)  #['apple', 'orange', 'mango']


methods:
1.append()--this method is used to add a new item into end of the list i.e.last index of list.

syntax:
variable_name.append(item)
'''

any = [1,"python",[1,2,[34,"this is python 3rd class",78],"python is a lang",89],34,[3,4]]
print(any[2][4])


any = [1,2,3]
any.append(6)
print(any)
any.append(20)
print(any)
any.append([20,90])
print(any)

'''
--> diff blw mutable and immutable?
2.Immutable- could not able to modify on that particular variable .

ex:
    int,str,float,tuple.

3.Mutable-can able to modify on that particular variable.

ex:
   list,set,dictionary
    
'''
so="python is a"
print(so.replace("python","java"))
print(so)

any = [1,2,3]
any.append(6)
print(any)

'''
diff blw append & extend?

-->append - Adds whole item as one element

5.extend - Adds items one by one
syntax:
     variable_name.extend(item)

both will add at the end only .
'''
any = [1,2,3]
any.append("python")
any.extend("python")
print(any)

'''
6.pop- removing the index value.
syntrax:
      variable_name.pop(index position)

7.remove-will remove value not index value.
syntax:
     variable_name.remove(item)
'''

any = [1,2,3]
any.pop(2)
print(any)


any = ["python",2,3,4]
any.remove(2)
print(any)






