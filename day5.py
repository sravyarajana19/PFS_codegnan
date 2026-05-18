'''
set:
    * A set is a collection of unique and unordered elements.
    * duplicate values are not allowed.
    * represented in {}.
    * items are not stored in index order.
syntax:
       
ex:
any = {1,2,3,4,2,5}
an = {10,50,30,80}
print(any | an)
print(any.union(an))
-------------------------------------------
methods:

1.Union():
it will give all values from 2 sets together at once.

syntax:
      variable_name.union(another var).

2. intersection():
it will gives the common values blw two sets.

syntax:
      variable_name.intersection(another var)

3.difference:
removing common values.

syntax:
      variable_name.difference(another var)

4.symmetric difference(^):
values except common.

syntax:
       variable_name.symentric_diff(another var)

5.add():
to add new elements into set

syntax:
    variable_name.add(element)

6.update:
to add multiple items into set.

syntax:
      variable_name.update([element])

7.remove:
used to remove element from the set , but it through error if element is not in the set.

syntax:
      variable_name.remove(element)

8.discard:
 used to remove element from the set , but it not through error if element is not in the set.   

syntax:
       varible_name.discard(element)
-----------------------------------------------------------------------------------------------------       
any = {1,2,3,4,2,5}
an = {5,7,3,2}
print(any & an)
print(any.intersection(an))


any = {1,2,3,4,2,5}
an = {5,7,3,2,4}
print(any - an)
print(an.difference(any))

any = {1,2,3,4}
any.add(41)
print(any)

any = {1,4,8,9}
any.update([23,78])
print(any)
           
any = {1,2,3,4}
any.min(41,1,3)
print(any)
''' 
