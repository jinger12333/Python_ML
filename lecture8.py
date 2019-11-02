#numpy array attributes and methods

import numpy as np
arr = np.arange(25)
ranarr = np.random.randint(0,50,10)

print(arr)
print(ranarr)

print(arr.reshape(5,5))#prints out 5 by 5 2d array, this case from 0 to 24

#max() |  min() returns the max and min of the array
#argmax() |  argmin()  returns the index of the max and min

print(ranarr.max(), ranarr.min())
print(ranarr.argmax(), ranarr.argmin())

print(arr.reshape(1,25))#reshapes the array (in this case) to 1 rows and 25 colums
print(arr.reshape(1,25).shape)#tells you how many rows and colums array has

#dtype
#you can grab the data type of the object in the array

print(arr.dtype)# in this case the data type is integer of 64 bits

#Numpy Indexing and Selection
#dissuss how to select elements or groups from an array

arr=np.arange(0,11)
print(arr)

#grab the value of an index
print(arr[8])

#get values in a range
print(arr[1:5])

#boardcasting
#numpy arrays differ from a normal python list because of their ability to boardcast

#setting a value with index range(boardcasting)
arr[0:5] =100#it has to be a numpy array
print(arr)

arr[5:8]

#reset to remove broadcast

arr = np.arange(0,11)
print(arr)

slice_of_arr = arr[0:6]
print(slice_of_arr)

slice_of_arr[:] = 99
print(slice_of_arr)
print(arr)#even if you slice a part of a numpy array and broadcast that part, 
#the original numpy array will be changed as well

#data is NOT copied in NumPy, it's a view of the oringal array!
#this avoids memory problems

# to get a copie, you need to be explict:
arr_copy =arr.copy()
print('arr:',arr)
print('arr_copy',arr_copy)

#indexing a 2D array (matrices)
#General format is arr_2dOW OF ARR2DROW,COL.
#use the comma notation for clarity

arr_2d =np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)

#indexing a row:
print(arr_2d[1])

#format is arr_2d[row][col] or arr_2d[row,col]
#getting an individual elements of values
print(arr_2d[1,0])#the second row, the first colum
print(arr_2d[2,2])#third row, third colum

#2D arrway slicing
#shape (2,2) from top right corner:
print(arr_2d[0:2,1:3]) #prints the values being overlapped by the row and colum
print(arr_2d[2,:])#third row, all of the colums
#the above and below are the same
print(arr_2d[2])#third row

#Fancy indexing
#fancy indexing allows you to select entire rows or colums OUT OF ORDER

#set up matrix
arr2d = np.zeros((10,10))

#length of the array:
arr_length = arr2d.shape[1]

#set up array 
for i in range(arr_length):
    arr2d[i] = i

print(arr2d)
print(arr2d[[2,4,6,8]])#grabs row 2, 4, 6, 8
print(arr2d[[8,1,7,3],[4]])#grabs parts of row 8,1,7,3 that is in colum 4
print(arr2d[[9,8,7,4],[3,4,5,6]])#grabs parts of row 9,8,7,4 that is in colum 3,4,5,6