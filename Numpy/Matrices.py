from numpy import *
A = array([[1,2,3,4],[5,5,5,1],[7,8,9,10],[2,2,2,2]])
B = array([[2,4,6,2],[6,8,6,1],[1,6,11,12],[1,1,1,1]])

m = matrix(A)
n = matrix(B)
mul = m*n
add = m + n
scalermul = 2*n
print(mul)
print(add)
print(scalermul) 

