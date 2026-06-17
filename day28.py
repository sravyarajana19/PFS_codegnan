'''
matplotlib: this is the libray in python for data visualization , allowing users to to create a vairety of plots.

basic structure of matplotlib:

> figures
> axes
> axis
> grid
> title
> legend
-------------------------------
import matplotlib.pyplot as plt
sales = ['A','B','C']
values = [25, 30, 45]
plt.bar(sales, values, color = 'red')
plt.xlabel('car modles')
plt.ylabel('values')
plt.title('BMW')
plt.show()
------------------------------
import  matplotlib.pyplot as plt
subjects = ['python','java','c']
students = [35,7,15]
plt.pie(students, labels = subjects,autopct = '%1.1f%%')
plt.legend(subjects)
plt.title('students in courses')
plt.show()
------------------------
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,15,18,20,13]

plt.scatter(x,y)
plt.title('scatter plot')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()
-----------------------------

import matplotlib.pyplot as plt
y = [10,20,30,40,50]

plt.hist(y, color = 'pink')
plt.title('Histogram plot')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()

---------------------------
'''
import matplotlib.pyplot as plt
sales = ['A','B','C']
values = [25, 30, 45]
plt.bar(sales, values, color = 'orange')
plt.xlabel('car modles')
plt.ylabel('values')
plt.title('Honda')
plt.show()




































