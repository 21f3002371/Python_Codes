def modified_bubble_sort(A):
    n = len(A)-1
    while n > 0:
        flag = False
        for i in range(n):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                flag = True
        if not flag:
            break
        n -= 1
    return A

print(modified_bubble_sort([1,2,3,4,5,6,7,8,99,8]))
