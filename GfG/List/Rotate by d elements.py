def rotateArr(arr,d):
        n = len(arr)
        d = d % n  # in case d > n
        arr[:] = arr[d:] + arr[:d]
        #The rotation is in-place
        return arr[:]
    
print(rotateArr([1,2,3,4,5],2))