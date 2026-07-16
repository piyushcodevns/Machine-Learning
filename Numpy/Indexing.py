import numpy as np

# Access Array Elements
arr=np.array([10,20,30,40,50,60,70,80,90,100])
print(arr[0])
print(arr[1])
print(arr[-4])
print(arr[2]+arr[3])

# Access 2-D Arrays
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0,1])
print(arr[1,4])

# Access 3-D Arrays
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[1,1,1])

# Negative Indexing
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,-1])