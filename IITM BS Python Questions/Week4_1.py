'''Accept a space-separated sequence of positive 
real numbers as input. 
Convert each element of the sequence into the 
greatest integer less than or equal to it. 
Print this sequence of integers as output, 
with a comma between consecutive integers.'''
from math import *
s = input().split()
for j in s:
    if j != s[-1]:
       print(floor(float(j)), end= ",")
    else:
        print(floor(float(s[-1])))
    
