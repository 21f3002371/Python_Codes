def isSorted(arr, n): 
    status = 0 
    if arr == sorted(arr):  
          status = 1 
    elif arr == sorted(arr, reverse=True): 
          status = 1
    return status

# Time Complexity O(nlogn), Space O(n)


def isSorted(arr, n):
    if n == 0 or n == 1:
        return 1  # empty or single-element array is sorted
    increasing = True
    decreasing = True

    for i in range(n-1):
          if arr[i] < arr[i+1]:
                 decreasing = False
          elif arr[i] > arr[i+1]:
                 increasing = False

          if increasing or decreasing:
                          return 1
          else:
                          return 0
                      
# Time Complexity O(n), Space O(1)
