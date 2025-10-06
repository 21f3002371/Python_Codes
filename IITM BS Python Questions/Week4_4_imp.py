# Print Identity Matrix
n = int(input())
A = [[] for i in range(n)]
for i in range(len(A)):
    for j in range(len(A)):
        if i != j:
            A[i].append(0)
        else:
            A[i].append(1)
        

     
print(A)
    