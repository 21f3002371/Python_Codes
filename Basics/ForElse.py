length = int(input())
A = []
for i in range(length):
    A.append(i)

for numbers in range(len(A)):
    if numbers == 67:
        print("67 exist in list")
        break
        
else:
    print("67 does not exist in list")