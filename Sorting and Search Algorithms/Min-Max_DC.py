def max_min(arr,lower,upper):
    if lower == upper: #only one element
        return arr[lower], arr[lower]
    elif lower == upper - 1: #Only two elements
        if arr[lower] > arr[upper]:
            return arr[lower], arr[upper]
        else:
            return arr[upper], arr[lower]
    else:
        mid = (lower+upper) // 2
        max1, min1 = max_min(arr, lower, mid)
        max2, min2 = max_min(arr, mid + 1, upper)
        return max(max1, max2), min(min1, min2)
    
                
A = [2,4,67,90,11,25,66,12,0,7]
lower = 0
upper = len(A)-1
maximum, minimum = max_min(A, lower, upper)
print("Maximum:", maximum)
print("Minimum:", minimum)
