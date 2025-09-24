n = int(input('Enter the length of string'))
A = []
for i in range(n):
    var = int(input())
    A.append(var)
    
Q = A[::-1] #Reversing a list
print(Q)