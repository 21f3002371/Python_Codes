# Remove Duplicates
A = [1,2,4,5,5,5,6,7,3,1,7,8,9,0,11]
dict = {}
for i in range(len(A)):
    if A[i] in dict.keys():
        dict[A[i]] += 1
    else:
        dict[A[i]] = 1
keys = dict.keys()
print(list(keys))