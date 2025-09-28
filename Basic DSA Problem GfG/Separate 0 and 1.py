A = [0,1,0,0,1,1,1,1,1,0,0,0]
count = 0
for i in range(len(A)):
    if A[i] == 0:
        count += 1
List_Separated = [0 for i in range(count)] + [1 for j in range(len(A)- count)]
print(List_Separated)