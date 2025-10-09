'''Given two integers n and m. 
You have to find the smallest modular
multiplicative inverse of n under modulo m. 
if it does not exist then return -1.'''
n = int(input())
m = int(input())
number = -1
for i in range(m):
    if (n*i)%m == 1:
        number = i
        
print(number)
                  