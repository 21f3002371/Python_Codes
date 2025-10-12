# Write a function named transpose 
# that accepts a matrix mat as input and returns its transpose.
n = int(input())
matrix = []
for i in range(n):
        val = list(map(int,input().split()))
        matrix.append(val)
    
transpose = [list(row) for row in zip(*matrix)]
print(transpose)
    