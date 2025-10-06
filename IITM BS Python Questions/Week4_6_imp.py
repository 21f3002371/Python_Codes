# Scaler Multiplication
n = int(input())
A = []
for i in range(n):
    s = list(map(int,input().split()))
    A.append(s)
B = []
for k in range(n):
    s = list(map(int,input().split()))
    B.append(s)
C = []    
for i in range(len(A)):
    row = []
    for j in range(len(A[i])):
        row.append(A[i][j] + B[i][j])
    C.append(row)
        
print(C)
        
    
    