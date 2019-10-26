'''
introduction to NumPy
NumPy or numpy is Linear Algebtra Liabrary for Python
Numpy is built on C libraries which makes it extremely fast for certain computations
'''
import numpy as np 
# NumPy arrays

#numpy arrays come in two flavours: vectors and matrices.
#Vectors are strickly 1-d arrays
# Matrics are 2-d or more , and they also have 1-d tho#


#vector
my_list = [1,2,3]
print(my_list)
np_list = np.array(my_list)
print(np_list)


#matrix
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
np_matrix = np.array(my_matrix)
print(np_matrix)#matrices ahve index as well as lists

#built-in Methods
#arrage
print(np.arange(0,10))#return evenly spaced values within a given interval
print(np.arange(0,100,5))

#zeros and ones
print(np.zeros(3))#Return a new array of given shape and type, filled with zeros
print(np.zeros((5,5)))
print(np.zeros(3))
print(np.zeros((3,3)))

#linspace
print(np.linspace(0,1,20))


#eye
print(np.eye(4))#Return a 2-D array with ones on the diagonal and zeros elsewhere

#Random
#rand - [0,1) uniform distribution (all numbers have the same chance)
print(np.random.rand(2))
print(np.random.rand(5,5))

#randn - standard normal distribution (numbers on the sides have less chance than numbers around 0)
print(np.random.randn(2))
print(np.random.randn(4,6))

#randint - low (inclusive) high (exclusive)
print(np.random.randint(5))
print(np.random.randint((5,5)))