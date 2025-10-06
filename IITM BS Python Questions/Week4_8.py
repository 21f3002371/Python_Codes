# Product of a Matrix
n = int(input())
A = []
for i in range(n):
    s = list(map(int,input().split()))
    A.append(s)
B = []
for j in range(n):
    s = list(map(int,input().split()))
    B.append(s)
C = []
for i in range(len(A)):
    row = []
   
    for p in range(len(B[0])):
        sum = 0
        for k in range(len(B)):
            sum += A[i][k]*B[k][p]
        row.append(sum)
    C.append(row)

    
print(C)
        