pos = -1
 # Initialize position variable to -1 (will store index if element is found)
def BinarySearch(arr,number):
    global pos
    l = 0                 # Lower bound index of search
    u = len(arr)-1        # Upper bound index of search
    while l <= u:
        mid = (l+u) // 2  # Find the middle index
        if (arr[mid] == number):
            pos = mid     # If found, store index in pos
            return True   # Return True if element is found
        elif arr[mid] < number:
            l = mid+1    # Search in the right half
        else:
            u = mid-1    # Search in the left half
    return False         # Return False if element is not found
list1 = [2,56,567,777,1233,8888,55555]
 # Example sorted list to search in
n = 777
 # Element to search for
if BinarySearch(list1,n):
    print("Element found at",pos+1)  # Output is 1-based index
else:
    print("Element not found")  # If not found, print message