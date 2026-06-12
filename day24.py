'''
regular expression or RegEx: is a sequence of characters that form a searching pattern.....
> this can be used to check if a string contain the specified search pattern ....
>python has buit in package called 're' which can be used to work with the regular expressions or regex..

--------------
functions in re:

1. findall --- Returns all matches in a list.
2. search --- Searches for a pattern anywhere in the string.
3. fullmatch --- Checks only from the beginning of the string.

---------------
meta char:

1. [] -- a-z, A-Z, 0-9 and any specified sequence...
2.  . -- each dot in one char...
3.  ^ -- looks for the string is starting with specified sequnce or not...
4.  $ -- looks for the string is ending with specified sequnce or not...
5.  * -- zero to more...
6.  ? -- zero or one...
7.  + -- one or more...
8.  {} -- print p word

----------------
special sequence:

1. \S -- no space
2. \s -- only space
3. \D -- except digits
4. \d -- only digits
5. \w -- matches any word char (letters, digits, underscore
6. \W -- non words
============================================================================
import re
txt = "cat bat rat"
x = re.findall("at", txt)
print(x)
-------------

import re
any_ = "python has buit in package called 're' which can be used to work with the "
print(re.search('[a]',any_)
--------------

import re
any_ = "python has buit in package called 're' which can be used to work with the "
print(re.search('pa.k..e',any_))
-----------------
import re
any_ = "python has buit in package called 're' which can be used to work python with the "
print(re.search('^python',any_))

import re
any_ = "python has buit in package called 're' which can be used to work python with the "
print(re.findall('^python',any_))
---------------------

import re
any_ = "python has buit in package called 're' which can be used to work python with the"
print(re.findall('the$',any_))

-------------------
import re
any_ = "python has buit in package called 're' which can be used to work python with the"
print(re.findall('p.* which',any_))
-------------------

import re
any_ = "python has buit in package called 're' which can be used to work python with the"
print(re.findall('p.?thon',any_))
-------------------

import re
any_ = "python has buit in package called 're' which can be used to work python with the"
print(re.findall('p.+',any_))
-------------------

import re
any_ = "python has buit in package called 're' which can be used to work python with the"
print(re.findall('py.{7}',any_))
-------------------

import re
any_ = "python has buit in package called 're' which can be used to work python with the"
print(re.findall('\S',any_))

import re
any_ = "python has buit in package called 're' which can be used to work python with the"
print(re.findall('\s',any_))

import re
any_ = "python has buit in package called 're' which can 23462 be used to work python with the"
print(re.findall('\D',any_))


import re
any_ = "python has buit in package called 're' which can 2346 be used to work python with the"
print(re.findall('\d',any_))


import re
any_ = "python has buit in package called 're' which can be used to work python with the"
print(re.findall('\w',any_))

import re
any_ = "python has buit in package @#$ called 're' which can be used %&^* to work python with the"
print(re.findall('\W',any_))
---------------------
'''

import re
mob_ = input("Enter the num: ")
so = re.fullmatch('[6-9][0-9]{9}',mob_)
if so:
    print(f"{mob_} this is valid indian number")
else:
    print(f"{mob_} this is invalid indian number")
    

 






















