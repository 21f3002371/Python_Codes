pos = -1
def linearsearch(list,n):
    found = False
    global pos
    for i in range(len(list)):
        if list[i] == n:
            pos = i+1
            found = True
    return found


list = [1,4,2,8,5,9,11,44,90]
n = 4
if linearsearch(list,n):
    print('Element found at',pos,"position")
else:
    print("Element not found")
