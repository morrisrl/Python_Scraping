# Team 05 Group HW 1 | February 21, 2018
# Rachel Morris, Rites Bhambhani, Michael Perry

# PART 1:

# 1) help(numpy)

# 2) NumPy
#___________________________________________________________
# PART 2:

# 1) The official URL is https://docs.scipy.org/doc/numpy/

# 2) NumPy stands for Numeric Python.

# 3) The name of the main objective provided by NumPy is ndarray.

# 4) The homogenous multidimensional array describes a table of items/elements (numbers), all of the same type, indexed by a tuple of positive integers.
#    Homogenous, in this case, means that they are all of the same type, and multidimensional means that there are many (N) integers. 

# 5) The six most important attributes are:
#    ndarray.ndim     - number of axes (dimensions) of the array, also known as rank
#    ndarray.shape    - dimensions of the array; in other words, a tuple of integers associated with the size of the array in each dimension
#    ndarray.size     - total number of elements of the array, equal to the product of elements of shape
#    ndarray.dtype    - object describing the type of elements in the array
#    ndarray.itemsize - size in bytes of each element of the array
#    ndarray.data     - buffer containing the elements of the array 

# 6) The items in a NumPy array can be changed with commands like reshape() and ravel(). The commands will return a modified array, but will not change the original.

# 7) You can access elements in a NumPy array by indexing like you can in lists, and you can also slice them. 
#___________________________________________________________
# PART 3:

# A)
import numpy as np
# 1)
    a = np.array([1,2,0])
    print(a)
#   >> [1 2 0]

# 2)
    b = np.array([(4,5,6), (7,8,9)])
    print(b)
#   >> [[4 5 6]
#       [7 8 9]]

# 3)
    print(a.dtype)
#   >> int64

# 4)
    print(a.shape)
#   >> (3,)        Shape describes n rows and n columns, respectively. 
    print(b.shape)
#   >> (2, 3)
    print(a.size)  Size describes the number of items in the array.
#   >> 3
    print(b.size)
#   >> 6
    print(a.ndim)  ndim describes how many dimensions are in the array.
#   >> 1
    print(b.ndim)
#   >> 2

# 5)
    c = a.view()
	c[2] = 3
	print(a)
#   >> [1 2 3]
#---------------------------------------------------------
# B)
# 6)
    scores_list = [35.5, 42, 39.2, 50, 47.7]
# 7)
    grades_list = [(score/50)*100 for score in scores_list]
    print(grades_list)
#   >> [71.0, 84.0, 78.4, 100.0, 95.4]
#---------------------------------------------------------
# C)
# 8)
    scores = np.array([35.5,42.0,39.2,50.0,47.7])

# 9)
    grades = (scores/50)*100  #directly convert our array into the grades
	print(grades)
#   >> [ 71.    84.    78.4  100.    95.4]

#10)
    print(grades.dtype)
#   >> float64
#----------------------------------------------------------
# D)
#11)
    length = [3, 2, 5, 1, 7]
    
#12)
    height = [4, 7, 5, 2, 3]
    
#13)
    l = np.array([3,2,5,1,7])
    
#14)
    h = np.array([4,7,5,2,3])
#-----------------------------------------------------------
# E)
# 15)
    area = [length[i]*height[i] for i in range(len(length))]
	print(area)
#   >> [12, 14, 25, 2, 21]
	print(sum(area))
#   >> 74
#------------------------------------------------------------
# F)
#16)
	w = np.array([2,6,1,8,4])
    area_array = l*w*h
    print(area_array)
#   >> [24 84 25 16 84]
#______________________________________________________________________________
# PART 4:
#      http://www.scipy-lectures.org/intro/numpy/index.html
#      This resource provides simple break downs of the arrays, reference documentation, creating the arrays, as well as divides 
#      it into clear sections on how to manipulate and use NumPy. It's also easy to navigate because it provides advanced 
#      operations and goes into detail on elaborate arrays if someone is more experienced and wants more in-depth practice.
#      I like the way this is set up because it's not a huge page full of tasks but rather breaks each part into steps, which makes
#      it extremely cohesive and easy to follow. 
