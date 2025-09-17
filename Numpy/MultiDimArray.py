from numpy import *
# Converting 2D array into 1D
arr1 = array([[1,2,3,4], [5,6,7,8]])
arr2  = arr1.flatten()
print(arr2)

# Converting 1D array in 3D
arr3 = arr2.reshape(4,-1) #reshape(dim1,dim2,dim3) # -1 adjusts array accordingly 
print(arr3)