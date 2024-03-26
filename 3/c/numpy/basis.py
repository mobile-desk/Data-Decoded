# install NumPy using "pip install numpy"

import numpy as np

#Initializing 1d array
a = np.array([1,2,3])
print(f"This is a 1d array {a}")
#Initializing 2d array
a = np.array([[1.5,2.5,3.5],[1,2,3]])
print(f"This is a 2d array {a}")
#Initializing 3d array
a = np.array([[[1,2,3],[4,5,6]],[[1.5,2.5,3.5],[4.5,5.5,6.5]]])
print(f"This is a 3d array {a}")

#check the dimension
print(a.ndim)

#get the shape
print(f"The shape {a.shape}")

#get the data type and memory size
print(f"Data type {a.dtype}")


#specify dtype during initialization
b = np.array([1,2,3], dtype='int16')

print(f'specified dtype {b.dtype}')

#Get size in bytes
print(f'{b.itemsize}')

#Get total elements
print(a.size)


#get total no of bytes
print(f"Total bytes {a.size * a.itemsize}")
print(f"Total bytes {a.nbytes}")
