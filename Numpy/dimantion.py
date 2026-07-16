# 0-D Arrays
import numpy as np
arr=np.array([42])
print(arr)

# 1-D Arrays
arr=np.array([1,2,3,4,5,6])
print(arr)

# 2-D Arrays
arr=np.array([1,2,3,4,5,6])
s=arr.reshape([2,3])
print(s)

arr=np.array([[1,2,3],[4,5,6]])
print(arr)

# 3-D Arrays
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
print(arr)

# Check dimention?
a=np.array([42])
b=np.array([1,2,3,4])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher Dimensional Arrays
arr=np.array([1,2,3,4], ndmin=5)
print(arr)
print(arr.ndim)