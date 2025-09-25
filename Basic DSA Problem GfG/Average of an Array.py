def AverageArray(A):
    n = len(A)
    sum = 0
    for i in A:
        sum += i
    average = sum//len(A)
    return average

n = int(input("Enter the length of Array"))
A = []
for i in range(n):
    var = int(input())
    A.append(var)
print(AverageArray(A))