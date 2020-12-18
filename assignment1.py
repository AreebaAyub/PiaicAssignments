# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YZ_RDFNAeR-TSXnhEDntf6fQC5zlDUGT
"""

import numpy as np

#Create a null vector of size 10 
np.zeros(10)

#Create a vector with values ranging from 10 to 49
x=np.arange(10,50)
print(x)

#Find the shape of previous array in question 3
np.shape(x)

#Print the type of the previous array in question 3
type(x)

np.__version__

#dimension of array
x.ndim

#Create a boolean array with all the True values
np.array(range(1,10),dtype=bool)

#Create a two dimensional array
np.array(range(9)).reshape(3,3)

#Create a three dimensional array
np.array(range(24)).reshape(2,3,4)

#Reverse a vector (first element becomes last)
np.flip(x,axis=None)

#Create a null vector of size 10 but the fifth value which is 1
x=np.zeros(10,dtype=int)
x[5]=1
print(x)

#Create a 3x3 identity matrix
np.identity(3)

#Convert the data type of the given array from int to float
arr = np.array([1, 2, 3, 4, 5])
arrfloat=arr.astype(np.float64)
print(arrfloat)

#Multiply arr1 with arr2
 arr1 = np.array([[1., 2., 3.],
                [4., 5., 6.]])  
arr2 = np.array([[0., 4., 1.],
              [7., 2., 12.]])

np.multiply(arr1,arr2)

#Make an array by comparing both the arrays provided above
comparison= arr1==arr2
print(comparison)

#odd numbers
x=np.array(range(10))
x[x % 2 == 1]

#Replace all odd numbers to -1 from previous array
x[x % 2 == 1]=-1
print(x)

#Replace the values of indexes 5,6,7 and 8 to 12
for a in [5,6,7,8]:
  x[a]=12
print(x)

#Create a 2d array with 1 on the border and 0 inside
x=np.zeros(9).reshape(3,3)
x[0,0]=1
#x[2,2]=1
print(x)



"""difficulty level medium"""

#Replace the value 5 to 12
arr2d = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
arr2d[1,1]=12
print(arr2d)

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#Convert all the values of 1st array to 64
arr3d[0,0]=64
print(arr3d)

#Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it
x=np.array(range(9)).reshape(3,3)
x[0]

#Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it
x[2,2]

#Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows
x[0:2,2:3]

#Create a 10x10 array with random values and find the minimum and maximum values
y=np.array(range(100)).reshape(10,10)
print(np.amin(y, axis=None)) #minimum value
print(np.amax(y))

#Find the common items between a and b
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)

#Find the positions where elements of a and b match
np.intersect1d(a,b,return_indices=True)

#Find all the values from array data where the values from array names are not equal to Will
import random
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randint(7, size=random.randrange(1,10))
print(np.where(names[data]!="Will"))

#Find all the values from array data where the values from array names are not equal to Will and Joe
data = np.random.randint(7, size=random.randrange(1,10))
print(np.where(names[data]!="Will") and np.where(names[data]!="Joe") )

"""**DIFFICULTY LEVEL HARD**"""

#Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.
np.arange(1,16).reshape(5,3)

#Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16
np.arange(1,17).reshape(2,2,4)

#Swap axes of the array you created in Question 32
x = np.array([[1,2,3]])
np.swapaxes(x,0,1)

#Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0
x=np.array(range(10))
x**1/2

#Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays
import random
a=np.random.randint(12,size=random.randrange(0,12))
b=np.random.randint(12,size=random.randrange(0,12))
np.where(a==b)

#Find the unique names and sort them out
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
np.unique(names)

#From array a remove all items present in array b
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
np.setdiff1d(a, b)

#Following is the input NumPy array delete column two and insert following new column in its place.
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
newColumn = np.array([[10,10,10]])
sampleArray[1]=newColumn
print(sampleArray)

#Find the dot product of the above two matrix
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
np.dot(x,y)

#Generate a matrix of 20 random values and find its cumulative sum
m=np.random.randint(20,size=(random.randint(0,5),random.randint(0,5)))
np.cumsum(m)