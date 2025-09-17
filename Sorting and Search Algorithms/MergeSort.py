def merge(arr, left, mid, right):
    n1 = mid - left + 1 # Length of Left half
    n2 = right - mid # Length of right alf

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i] # Fill left subarray
    for j in range(n2):
        R[j] = arr[mid + 1 + j] # Fill right subarray
        
    i = 0  # Index for left subarray L
    j = 0  # Index for right subarray R
    k = left # Index for main array arr 

    # Merge the temp arrays back
    # into arr[left..right]
    # This loop keeps picking the smaller element from L and R and puts it back into arr.
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[],if there are any 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# MAIN FUNCTION
def mergeSort(arr, left, right):
    if left < right: # At least two elements
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)
        
    return arr

A = [1,4,1,2,4,7,88,33,22,6,76]

print(mergeSort(A,0,len(A)-1))