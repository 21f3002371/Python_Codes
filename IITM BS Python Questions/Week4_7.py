# Find median
n = int(input())
A= []
def sortfunc(list1):
    j = len(list1)-1
    while j >0:
        for i in range(j):
            if list1[i] > list1[i+1]:
                list1[i],list1[i+1] = list1[i+1],list1[i]
                
        j -= 1
    return list1
    
for i in range(n):
    var = int(input())
    A.append(var)
s = sortfunc(A)
median = 0
mid = len(s)/2
for i in range((len(s))):
    if len(s)%2 == 0:
        median = (s[int(mid)] + s[int(mid)+1])/2
    else:
        median = s[int(mid)]
        
print(f'Median of {A} is {median}')