'''Accept a square matrix as input and
store it in a variable named matrix.
The first line of input will be n, the number of rows 
in the matrix. 
Each of the next n lines will have a sequence of n
space-separated integers.
'''
n = int(input())
A = []
for i in range(n):
        s = input().split()
        for j in range(len(s)):
            s[j] = int(s[j])
        A.append(s)
        
print(A)