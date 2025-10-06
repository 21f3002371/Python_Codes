# Find nearest distance
'''
First line is integer n
next n lines represent points
the last line represent the coordinate p(x,y) and the goal
is to find minimum from point p.

3
1,2
3,5
6,12
4,6
'''
from math import *
A = []
n = int(input())
for i in range(n):
    s = list(map(int,input().split(',')))
    A.append(s)
p = list(map(int,input().split(',')))
x  = p[0]
y = p[1]
distance_list = []
for i in range(n):
  
     distance_list.append(sqrt((A[i][0]-x)**2 + (A[i][1]-y)**2))

a = min(distance_list)
for i in range(len(distance_list)):
    if distance_list[i] == a:
        print(A[i])

        