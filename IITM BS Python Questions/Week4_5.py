# Scaler Multiplication of Matrix
Matrix  = []
n = int(input())
for i in range(n):
    s = input().split()
    for j in range(len(s)):
        s[j] = int(s[j])
    Matrix.append(s)
    
scaler = int(input())
for i in range(n):
    for j in range(len(Matrix[i])):
        Matrix[i][j] = scaler*Matrix[i][j]
        
print(Matrix)
    
    