"""
No Copy : Variable assignment, ids of the objects will be same.
"""
import numpy as np
arr_x = np.arange(6)
arr_y = arr_x
print(id(arr_x))
print(id(arr_y))


"""
View: This is also known as Shallow Copy. 
The view is just a view of the original array and view does not own the data(ids will be different). 
When we make changes to the view it affects the original array, 
and when changes are made to the original array it affects the view.
"""
import numpy as np
arr_x = np.arange(6)
arr_v = arr_x.view()
print(id(arr_x))
print(id(arr_v))

arr_x[0] = 100
print(arr_x)
print(arr_v)

arr_v[1] = 101
print(arr_x)
print(arr_v)


"""
Copy: This is also known as Deep Copy. 
The copy is completely a new array and copy owns the data. 
When we make changes to the copy it does not affect the original array, 
and when changes are made to the original array it does not affect the copy.
"""
import numpy as np

arr_x = np.array([2, 4, 6, 8, 10])
arr_c = arr_x.copy()

print(id(arr_x))
print(id(arr_c))

arr_x[0] = 100
print(arr_x)
print(arr_c)

arr_c[1] = 200
print(arr_x)
print(arr_c)


"""
Horizontal Stack
"""
import numpy as np
arr_x = np.array([[1,2,3], [-1,-2,-3]])
arr_y = np.array([[4,5,6], [-4,-5,-6]])
arr = np.hstack((arr_x, arr_y))
print(arr)


"""
Vertical Stack
"""
import numpy as np
arr_x = np.array([[1,2,3], [-1,-2,-3]])
arr_y = np.array([[4,5,6], [-4,-5,-6]])
arr = np.vstack((arr_x, arr_y))
print(arr)


"""
Concatenate
"""
import numpy as np  
arr_x = np.array([[1, 2], [3, 4]])
arr_y = np.array([[5, 6], [7, 8]])
arr_h = np.concatenate((arr_x, arr_y), axis=0)
arr_v = np.concatenate((arr_x, arr_y), axis=1)
print(arr_h)
print(arr_v)


"""
Combining a one and a two-dimensional NumPy Array
"""
import numpy as np
  
arr1 = np.arange(5)
arr2 = np.arange(10).reshape(2,5)
  
for a, b in np.nditer([arr1, arr2]):
    print((int(a), int(b)))


"""
Compare numpy arrays
"""
import numpy as np
np1 = np.array([[1, 2], [3, 4]])
np2 = np.array([[1, 2], [3, 4]])
comparison = np1 == np2
i = comparison.all()
print(i)


"""
union of two numpy arrays and removes duplicates
"""
import numpy as np
arr_1 = np.array([10, 20, 30, 40])
arr_2 = np.array([20, 40, 60, 80])
arr = np.union1d(arr_1, arr_2)
print(arr)


"""
To identify unique elements, rows and columns
"""
import numpy as np

arr = np.array([[11, 11, 12, 11],
                [13, 11, 12, 11],
                [16, 11, 12, 11],
                [11, 11, 12, 11]])

arr_0 = np.unique(arr)
print(arr_0)
arr_1 = np.unique(arr, axis=0)
print(arr_1)
arr_2 = np.unique(arr, axis=1)
print(arr_2)


"""
1. Trim zeros from numpy array
2. "f" parameter trim leading zeros
3. "b" parameter trim trailing zeros
"""
import numpy as np

arr = np.array((0, 0, 0, 0, 1, 5, 7, 0, 6, 2, 9, 0, 10, 0, 0))
trim = np.trim_zeros(arr)
print(trim)
trim_f = np.trim_zeros(arr, "f")
print(trim_f)
trim_b = np.trim_zeros(arr, "b")
print(trim_b)


"""
Check whether a Numpy array contains a specified row
"""
import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]])

print([1, 2, 3, 4, 5] in array.tolist())


"""
How to Remove rows in Numpy array that contains non-numeric values?
Here axis 0 is the columns and axis 1 is the rows
"""
import numpy as np

array = np.array([[10.5, 22.5, 3.8], 
                  [23.45, 50, 78.7],
                  [41, np.nan, np.nan]])

print(array[~np.isnan(array).any(axis=1)])


"""
Remove single dimensional entries from the shape
"""
import numpy as np

array = np.array([[[2, 2, 2], [2, 2, 2]]])
print(np.squeeze(array))


"""
Find the number of occurrences of a sequence in a NumPy array
"""
import numpy as np
  
array = np.array([[2, 8, 9, 4], 
                  [9, 4, 9, 4],
                  [4, 5, 9, 7],
                  [2, 9, 4, 3]])

output = repr(array).count("9, 4")
print(output)


"""
Find most common pair in NumPy array
"""
import numpy as np

array = np.array([[2, 8, 9, 4], 
                  [9, 4, 9, 4],
                  [4, 5, 9, 7],
                  [2, 9, 4, 3]])

flat = array.flatten()

d  = dict()
for i in range(0, len(flat)-1):
        comb = (flat[i], flat[i+1])
        if comb in d.keys():
            d[comb] += 1
        else:
            d[comb] = 1

sorted = sorted(d.items(), key=lambda t: t[1], reverse=True)
print(sorted[0][0])


"""
How to check whether specified values are 
present in n*n NumPy?
"""
import numpy as np
  
np1 = np.array([[2, 3, 0],
               [4, 1, 6]])
print(10 in np1)


"""
How to get the diagonal elements of
n*n matrix
"""
import numpy as np
  
np1 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
res = np.diagonal(np1)
print(res)


"""
Count the number of non zero values in the array
"""
import numpy as np
  
np1 = np.array([[0, 2, 0], [0, 5, 0], [0, 8, 0]])
res = np.count_nonzero(np1)
print(res)


"""
How to find the size of an array
"""
import numpy as np

np1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(np.size(np1))
print(np.size(np1, 0)) 
print(np.size(np1, 1))


"""
How to reverse the numpy array
"""
import numpy as np
 
np1 = np.array([1, 2, 3, 6, 4, 5])
res = np.flip(np1)
print(res)


"""
How to make numpy readonly
"""
import numpy as np

a = np.zeros(11)
a.setflags(write=False)


"""
insert new column at position 2
"""
import numpy as np

twoDArray = np.array([["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]])
newTwoDArray = np.insert(twoDArray, 2, [[1,2,3]], axis=1)
print(newTwoDArray)

"""
insert new row at last
"""
import numpy as np

twoDArray = np.array([["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]])
newTwoDArray = np.append(twoDArray, [[1,2,3]], axis=0)
print(newTwoDArray)

"""
delete first column
"""
import numpy as np

twoDArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
newTwoDArray = np.delete(twoDArray, 0, axis=1)
print(newTwoDArray)