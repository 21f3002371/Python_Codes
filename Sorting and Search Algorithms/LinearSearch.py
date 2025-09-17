A = [1,2,56,78,90,23,35]
a = 90
found = False
for i in range(len(A)):
    if A[i] == a:
        print("The element found at",i)
        found = True
        break
if not found: # not found even after checking all elements
        print("Element not found")  
# This search is linear, checking each element until it finds the target.