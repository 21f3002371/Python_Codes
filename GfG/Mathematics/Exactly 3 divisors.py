'''Given a positive integer value n. 
The task is to find how many numbers less than or 
equal to n have numbers of divisors exactly 3.'''
'''def divisorthree(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count += 1
            
    if count == 3:
        return True
    return False
final = 0
n = int(input())
for j in range(n+1):
    if divisorthree(j):
        final += 1
        
print(final)'''

# A number has exactly three divisor if and only if it is 
# square of a prime number
def isprime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

n = int(input())
final = 0
for i in range(2,int(n**0.5)+1):
    if isprime(i) and i*i <= n:
        final += 1
        
print(final)
        
