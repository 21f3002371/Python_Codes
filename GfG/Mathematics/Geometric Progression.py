'''Given the first 2 terms a and b of a Geometric Series. 
The task is to find the nth term of the series.'''
a  = int(input())
b = int(input())
n = int(input())
r = b/a
print(int(a*(r**(n-1))))