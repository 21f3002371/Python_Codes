def immediateGreater(arr,x):
    arr.sort()
    larger = -1
    for i in arr:
        if i <= x:
            continue
        else:
            larger = i
            break
    return larger


A = list(map(int,input().split()))
n = int(input('Enter the number:'))
print(immediateGreater(A,n))