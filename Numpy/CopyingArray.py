from numpy import *
arr1 = [1,6,8,12,15]
arr2 = arr1.copy()
arr1[1] = 0
print(arr1)
print(arr2)

#view() function does the shallow copying, changing one array would change the other too