#Numpy Array Selection
# Go over how to use brackets for selection based off of comparison operators
# < > <= >= == etc#

import numpy as np

arr = np.arange(1,11)
print(arr)
print(arr>4)

#similar to filter functions in regular python
bool_arr = arr > 4
print(bool_arr)
#Selecting values that are True in the bool_arr, and leaves out the False
print (arr[bool_arr])
#or
print(arr[arr>9])
#or
x=2
print (arr[arr > x])

#arithmetic
#perform zrray with array arithmetic, or scaler (normal values, not arrays) with array arithmetics.
arr = np.arange( 0 ,10 )
print(arr)
print( arr+arr )#in np, the values of two lists will actually merge if you add them together.
print( arr*arr )#nultiplication also works
print( arr /arr) #LOL NAN
print(arr - arr)
print(arr**arr)#i think this is 'to the power of'
print(1+arr)
print(1/arr)

#universal Array Function
#essentially just mathematical operations you can use to perform the operation acroos the array

#taking square roots
print(np.sqrt(arr))

#calculating exponential (e^ - natural number
print(np.exp(arr))

#MAX, MIN, ETC
print(np.max(arr))

#trigonometery
print (np.sin(arr))
print (np.cos(arr))
print (np.tan(arr))

#logarithm
print(np.log(arr))
#2*3=6
#6 log 2 = 3                       
print("# Practice\n")
mat = np.arange(1,26).reshape(5,5)
print(mat)
print('\n[[12,13,14,15]\n\
    [17,18,19,10]\n\
    [22,23,24,25]]')

anwer = mat[2:,1:] #colums, rows
print(anwer)

import pandas as pd
#introduction to pandas#use panadas for data analysis, 
# basically an extremely powerful version of excel or Google Sheets, but with more features!ANCHOR
#Series, DataFrames, Missing Data, GroupBy, Merging, joining, and Conatenating, Operations, 
#data input and output

#series
#very similar to Numpy array (it is built ontop of the Numpy array object). What is different is that series can have
#axis labels, meaning it can be indexed by a label, instead of just a number location. It also doesn't need to 
#hold numeric data, it can hold any arbitrary Python Object.

labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array ([40,50,60])
d = {'a':70, 'b':80, 'c':90}

print(pd.Series (data = my_list, index=labels))

print(pd.Series(arr))
print(pd.Series(arr,labels))

print(pd.Series(d))

#Data in a Series
#pandas Series can hold a varity of object types

print(pd. Series(data= labels))
print(pd.Series([sum, print, len, max]))

ser1 =pd.Series([1,2,0,3,4],index = ["USA","GERM",'ITLAY',"USSR","CHINA"])
ser2 =pd.Series([1,2,5,0,4], index = ['USA','GERM','ITALY','USSR','CHINA'])
print(ser1,'\n', ser2)
print(ser1 +ser2)

#DataFrames Definition:
#The workhorses of pandas and are directly inspired by the R programming language. 
#DataFrames are a bunch of Series objects, put together to share the same index!

np.random.seed(101)
print(np.random.randn(5,4))
df = pd.DataFrame(np.random.randn(
    5, 4), index = 'A B C D E'.split(), columns= 'W X Y Z'.split())
print(df)
print(df['W'])
print(df[['W','Z']])
#print(df.w) <----don't use this syntax!

print(type(df), type(df['W']))
#creating a new column
df['Michael'] = df['W'] + df['Y']
print(df)

#remove existing column
df.drop('Michael', axis = 1, inplace=True)
# df = df.drop('Michael', axis = 1) same as line above
print(df)

#drop existin rows
df.drop('E', axis = 0, inplace=True)
print(df)

#selection of rows
print(df.loc['A'])
#select based off of position instead of label
print(df.iloc[2])

#selecting subset of rows and columns
print(df.loc['B','Y'])
print(df.loc[['A','B']])
