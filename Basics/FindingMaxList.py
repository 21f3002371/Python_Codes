max = 0
A = [1,34,67,98, 234,54,-51,91]
for i in range(len(A)):
    if A[i] > max:
        max = A[i]
print(max)