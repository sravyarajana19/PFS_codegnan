'''
Data Analysis: this is process of isnspecting , cleaning , transforming, and modeling data to discover useful insights......
-------------

types of da:

1. descriptive analysis --> summarizing data

2. diagnostic analysis: -- > understanding causes

3. predictive analysis:--> forecasting future outcomes

4. prescriptive analysis: --> suggesting actings based on data

------------------

why da:

> to improve decision making
> detects trends and patterns

---------------------

numpy: array concept in python(numerical python)

this python library for numerical computing . It provides support for multi - dimentional arrays, and linear algebra operations, making it essential for data analysis.....

using numpy in da:

> improve performance
> simplifies complex operations
> easy data manipulation


import numpy as np
a = np.array([[1, 2, 3, 4],[2, 3, 4, 5],[6, 7, 8, 9]])
print(a)

import numpy as np
a = np.array([[1, 2, 3, 4],[2, 3, 4, 5],[6, 7, 8, 9]])
print(a)
print(a.shape)

import numpy as np
a = np.array([[1, 2, 3, 4],[2, 3, 4, 5]])
print(a)
print(a.shape)
reshaped = a.reshape(4, 2)
print(reshaped)
------------------
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))
    (or)
import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print(np.dot(a, b))
------------------
>> Shallow Copy → Shares inside data
>> Deep Copy    → Duplicates everything

import copy
a = [[1, 2], [3, 4]]
b = copy.copy(a)   # Shallow copy
b[0][0] = 100

print(a)
print(b)


import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0][0] = 100

print(a)
print(b)
--------------
pandas :
> the pandas is a powerful data manipulation and data analysis
> where it provides data structure like series and dataframe for efficient data handling....

import pandas as pd
a= pd.Series([2999,159999,49999, 19999, 39999],
             index = ['earbuds','smartphone','lap','watch','footwear'])
print(a)


dataframes
----------
'''
import pandas as pd
data = {
    'product':['earbuds','smartphone','lap','watch','footwear'],
    'Brand':['noise','oneplus','hp','bolt','nike'],
    'price':[1599, 2999, 39999, 4999,6999],
    'stock':[50,15,25,40,70]
    }
dip = pd.DataFrame(data)
print(dip)


























































