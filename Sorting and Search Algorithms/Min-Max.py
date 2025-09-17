a = [16,18,7,5,23,67,44]
max = a[0]
min = a[0]
for i in range(len(a)):
    if max < a[i]:
     max = a[i]
    elif min > a[i]:
     min = a[i]

print(max,min)
    
