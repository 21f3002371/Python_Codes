# Binary Search
pos = -1
def RecursiveBinarySearch(arr,number,l,u):
    global pos
    if l > u:
        return False
    else:
           mid  = (l+u) // 2
           if (arr[mid] == number):
               pos = mid
               return True
           elif arr[mid] < number:
               return RecursiveBinarySearch(arr,number,mid+1,u) #Do not slice the arr
           else:
               return RecursiveBinarySearch(arr,number,l,mid-1)
    return False
        
A = [1,2,3,4,5,6,7,8,9,10]
n = 10
if RecursiveBinarySearch(A,n,0,len(A)-1):
    print("Element found at",pos+1)
else:
    print("Element not found")