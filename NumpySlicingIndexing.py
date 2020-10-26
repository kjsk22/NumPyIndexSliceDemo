import numpy as np
#create numpy array
a = np.arange(9)
a

#get the element from array with index 5
a[5]

#get elements from 0 to 4
a[0:5]

#get last but one element
a[-2]

#get elements from 6 to 8
xy = a[6:9]
xy

#reshape the array to 3 by 3
a = np.arange(9).reshape(3,3)
a

#get element with index 1 in row and index 1 in column
a[1,1]

#get all rows and index 1 column

a[:,1]
a[:,-1]
a[1:3,1:3]
#create new array
b = np.arange(10,19).reshape(3,3)
b
#traverse through rows
for row in b:
    print(row)

#flatten and traverse through all elements
for element in b.flatten():
    print(element)

#vertical stack two arrays
np.concatenate((a,b))
np.vstack((a,b))

#horizontal stack two arrays
np.concatenate((a,b), axis=1)
np.hstack((a,b))

#create a new 3 by 4 array
c = np.arange(12).reshape(3,4)
c

#split along vertical axis into 3
np.vsplit(c,3)

#split along horizontal axis into 4
np.hsplit(c,4)

#create boolean array satisfying condition C>5
d = c>5
d
#assign 22 for elements in C where condition is satisfied
c[d] = 22
c































