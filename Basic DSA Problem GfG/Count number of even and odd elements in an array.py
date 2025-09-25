n = int(input())
A  = []
count_even = 0
count_odd = 0
for i in range(n):
    var = int(input())
    A.append(var)
for j in A:
    if j%2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(A,count_even,count_odd)
