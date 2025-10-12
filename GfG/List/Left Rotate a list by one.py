A = [20,20,30,40,70]
B = []
for i in range(len(A)):
    B.append(A[(i+1)%len(A)])

print(B)